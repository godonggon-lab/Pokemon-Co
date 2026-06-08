from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    m, _n = map(int, lines[0].split())
    universes = []
    for line in lines[1:1 + m]:
        arr = list(map(int, line.split()))
        order = {value: index for index, value in enumerate(sorted(set(arr)))}
        universes.append(tuple(order[value] for value in arr))
    answer = 0
    for i in range(m):
        for j in range(i + 1, m):
            if universes[i] == universes[j]:
                answer += 1
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 3\n1 2 3\n10 20 30\n"),
        edge("2 3\n1 1 2\n3 3 4\n"),
        edge("3 2\n1 2\n2 1\n10 20\n"),
        edge("3 3\n3 2 1\n30 20 10\n1 2 3\n"),
        edge("4 3\n1 1 1\n2 2 2\n3 3 3\n1 2 3\n"),
        stress("4 4\n1 2 3 4\n4 3 2 1\n10 20 30 40\n5 5 6 7\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
