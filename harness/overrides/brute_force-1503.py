from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    target, bad_count = map(int, lines[0].split())
    bad = set(map(int, lines[1].split())) if bad_count else set()
    good = [value for value in range(1, 1002) if value not in bad]
    good_set = set(good)
    answer = 10**18
    for a in good:
        for b in good:
            base = target // (a * b)
            for c in range(max(1, base - 2), min(1001, base + 2) + 1):
                if c in good_set:
                    answer = min(answer, abs(target - a * b * c))
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("10 0\n"),
        edge("10 3\n1 2 3\n"),
        edge("100 5\n1 5 10 20 25\n"),
        edge("1 1\n1\n"),
        edge("27 2\n3 9\n"),
        stress("500 10\n" + " ".join(str(i) for i in range(1, 11)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
