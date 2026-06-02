from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    score = [list(map(int, line.split())) for line in lines[1:1 + n]]
    answer = 10**9
    full = (1 << n) - 1
    for mask in range(1, full):
        other = full ^ mask
        if mask > other:
            continue
        start = [i for i in range(n) if mask & (1 << i)]
        link = [i for i in range(n) if other & (1 << i)]
        start_score = sum(score[a][b] + score[b][a] for i, a in enumerate(start) for b in start[i + 1:])
        link_score = sum(score[a][b] + score[b][a] for i, a in enumerate(link) for b in link[i + 1:])
        answer = min(answer, abs(start_score - link_score))
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n0 1\n2 0\n"),
        edge("4\n0 1 2 3\n4 0 5 6\n7 1 0 2\n3 4 5 0\n"),
        edge("4\n0 1 1 1\n1 0 1 1\n1 1 0 1\n1 1 1 0\n"),
        edge("6\n0 1 2 3 4 5\n1 0 2 3 4 5\n1 2 0 3 4 5\n1 2 3 0 4 5\n1 2 3 4 0 5\n1 2 3 4 5 0\n"),
        edge("6\n0 5 4 3 2 1\n1 0 5 4 3 2\n2 1 0 5 4 3\n3 2 1 0 5 4\n4 3 2 1 0 5\n5 4 3 2 1 0\n"),
        stress("8\n0 1 2 3 4 5 6 7\n7 0 1 2 3 4 5 6\n6 7 0 1 2 3 4 5\n5 6 7 0 1 2 3 4\n4 5 6 7 0 1 2 3\n3 4 5 6 7 0 1 2\n2 3 4 5 6 7 0 1\n1 2 3 4 5 6 7 0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
