from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    k, n, f = map(int, lines[0].split())
    relation = [[i == j for j in range(n + 1)] for i in range(n + 1)]
    for line in lines[1:1 + f]:
        a, b = map(int, line.split())
        relation[a][b] = relation[b][a] = True
    answer: list[int] | None = None
    chosen: list[int] = []

    def dfs(start: int) -> bool:
        nonlocal answer
        if len(chosen) == k:
            answer = chosen[:]
            return True
        for person in range(start, n + 1):
            if all(relation[person][friend] for friend in chosen):
                chosen.append(person)
                if dfs(person + 1):
                    return True
                chosen.pop()
        return False

    dfs(1)
    if answer is None:
        return "-1"
    return "\n".join(map(str, answer))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1 0\n"),
        edge("2 3 1\n1 2\n"),
        edge("3 3 3\n1 2\n1 3\n2 3\n"),
        edge("3 4 2\n1 2\n3 4\n"),
        edge("3 5 6\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n"),
        stress("4 6 9\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4\n3 5\n4 5\n5 6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
