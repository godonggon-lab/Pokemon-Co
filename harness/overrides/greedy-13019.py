from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('ABC\nBCA\n', '2\r\n'),
        edge('ABC\nDEF\n', '-1\r\n'),
        edge('A\nA\n', '0\r\n'),
        edge('ABC\nCAB\n', '1\r\n'),
        edge('AABC\nABCA\n', '3\r\n'),
        stress('AABBC\nBACAB\n', '3\r\n'),
    ]
