from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('ABC\nBCA\n', '2\r\n'),
        edge('ABC\nDEF\n', '-1\r\n'),
        stress('AABBC\nBACAB\n', '3\r\n'),
    ]
