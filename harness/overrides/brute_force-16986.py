from __future__ import annotations
import itertools
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, k = map(int, lines[0].split())
    win = [list(map(int, line.split())) for line in lines[1:1 + n]]
    seq = [
        [],
        [x - 1 for x in map(int, lines[1 + n].split())],
        [x - 1 for x in map(int, lines[2 + n].split())],
    ]

    def can(order: tuple[int, ...]) -> bool:
        index = [0, 0, 0]
        score = [0, 0, 0]
        p1, p2 = 0, 1
        while True:
            if score[0] >= k:
                return True
            if score[1] >= k or score[2] >= k:
                return False
            if index[0] >= n:
                return False
            h1 = order[index[0]] if p1 == 0 else seq[p1][index[p1]]
            h2 = order[index[0]] if p2 == 0 else seq[p2][index[p2]]
            index[p1] += 1
            index[p2] += 1
            if win[h1][h2] == 2:
                winner = p1
            elif win[h1][h2] == 0:
                winner = p2
            else:
                winner = max(p1, p2)
            score[winner] += 1
            p1, p2 = winner, 3 - p1 - p2

    return "1" if any(can(order) for order in itertools.permutations(range(n))) else "0"

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3 2\n1 2 0\n0 1 2\n2 0 1\n1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2\n2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3\n"),
        edge("2 2\n1 2\n0 1\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n"),
        stress("4 3\n1 2 0 2\n0 1 2 0\n2 0 1 2\n0 2 0 1\n1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4\n4 3 2 1 4 3 2 1 4 3 2 1 4 3 2 1 4 3 2 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
