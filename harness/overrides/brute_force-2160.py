from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    pictures = ["".join(lines[1 + i * 5:1 + (i + 1) * 5]) for i in range(n)]
    best = (10**9, 1, 2)
    for i in range(n):
        for j in range(i + 1, n):
            diff = sum(a != b for a, b in zip(pictures[i], pictures[j]))
            if diff < best[0]:
                best = (diff, i + 1, j + 1)
    return f"{best[1]} {best[2]}"

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n.....\n.....\n.....\n.....\n.....\n#####\n#####\n#####\n#####\n#####\n"),
        edge("2\n.....\n.....\n.....\n.....\n.....\n.....\n.....\n.....\n.....\n.....\n"),
        edge("3\n#....\n.....\n.....\n.....\n.....\n.#...\n.....\n.....\n.....\n.....\n#####\n#####\n#####\n#####\n#####\n"),
        edge("3\n#####\n.....\n#####\n.....\n#####\n#####\n.....\n#####\n.....\n####.\n.....\n#####\n.....\n#####\n.....\n"),
        edge("4\n.....\n.....\n.....\n.....\n....#\n.....\n.....\n.....\n.....\n.....\n.....\n.....\n.....\n.....\n...#.\n#####\n#####\n#####\n#####\n#####\n.....\n.....\n.....\n.....\n.....\n"),
        stress("3\n.....\n.....\n.....\n.....\n.....\n....#\n.....\n.....\n.....\n.....\n#####\n#####\n#####\n#####\n#####\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
