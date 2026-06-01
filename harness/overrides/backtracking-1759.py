from __future__ import annotations

from itertools import combinations
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    length, _ = map(int, lines[0].split())
    letters = sorted(lines[1].split())
    vowels = set("aeiou")
    rows = []
    for chosen in combinations(letters, length):
        vowel_count = sum(letter in vowels for letter in chosen)
        if vowel_count >= 1 and length - vowel_count >= 2:
            rows.append("".join(chosen))
    return "\n".join(rows)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("4 6\na t c i s w\n"),
        edge("3 5\na b c d e\n"),
        edge("2 4\na b c d\n"),
        edge("5 7\na e i b c d f\n"),
        stress("6 10\na b c d e f g h i j\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
