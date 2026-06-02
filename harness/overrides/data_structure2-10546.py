from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    counts: dict[str, int] = {}
    for name in lines[1:1 + n]:
        counts[name] = counts.get(name, 0) + 1
    for name in lines[1 + n:1 + n + n - 1]:
        counts[name] -= 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[0][0]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\nleo\n"),
        edge("2\nleo\nkiki\nleo\n"),
        edge("3\nalice\nbob\nalice\nalice\nbob\n"),
        edge("4\nmislav\nstanko\nmislav\nana\nstanko\nana\nmislav\n"),
        edge("5\na\na\nb\nb\nc\na\nb\nb\nc\n"),
        stress("6\nrunner1\nrunner2\nrunner3\nrunner2\nrunner4\nrunner5\nrunner1\nrunner2\nrunner3\nrunner4\nrunner5\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
