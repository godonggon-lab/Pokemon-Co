from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nbook\n"),
        edge("2\na\nb\n"),
        edge("3\na\nb\na\n"),
        edge("5\ntop\ntop\nalpha\nalpha\nzeta\n"),
        edge("6\nz\nx\ny\nx\ny\nz\n"),
        stress("10\npython\ncpp\njava\npython\njava\npython\nrust\ncpp\ncpp\ncpp\n"),
    ]
