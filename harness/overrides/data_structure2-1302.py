from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    counts: dict[str, int] = {}
    for title in lines[1:1 + n]:
        counts[title] = counts.get(title, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[0][0]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\nbook\n"),
        edge("2\na\nb\n"),
        edge("3\na\nb\na\n"),
        edge("5\ntop\ntop\nalpha\nalpha\nzeta\n"),
        edge("6\nz\nx\ny\nx\ny\nz\n"),
        stress("10\npython\ncpp\njava\npython\njava\npython\nrust\ncpp\ncpp\ncpp\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
