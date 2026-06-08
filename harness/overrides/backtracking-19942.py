from __future__ import annotations
from itertools import combinations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    need = list(map(int, lines[1].split()))
    foods = [list(map(int, line.split())) for line in lines[2:2 + n]]
    best_cost = 10**18
    best_indices: list[int] | None = None
    for size in range(1, n + 1):
        for selected in combinations(range(n), size):
            total = [0, 0, 0, 0, 0]
            for index in selected:
                for col in range(5):
                    total[col] += foods[index][col]
            if all(total[col] >= need[col] for col in range(4)):
                indices = [index + 1 for index in selected]
                if total[4] < best_cost or (total[4] == best_cost and (best_indices is None or indices < best_indices)):
                    best_cost = total[4]
                    best_indices = indices
    if best_indices is None:
        return "-1"
    return f"{best_cost}\n{' '.join(map(str, best_indices))}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 1 1 1\n1 1 1 1 5\n"),
        edge("3\n10 10 10 10\n10 0 0 0 5\n0 10 0 0 6\n0 0 10 10 7\n"),
        edge("2\n10 10 10 10\n1 1 1 1 1\n2 2 2 2 2\n"),
        edge("4\n5 5 5 5\n5 5 0 0 10\n0 0 5 5 8\n3 3 3 3 6\n10 10 10 10 50\n"),
        edge("3\n5 5 5 5\n5 5 5 5 10\n5 5 5 5 10\n5 5 5 5 9\n"),
        stress("5\n15 15 15 15\n10 5 5 5 10\n5 10 5 5 10\n5 5 10 5 10\n5 5 5 10 10\n20 20 20 20 100\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
