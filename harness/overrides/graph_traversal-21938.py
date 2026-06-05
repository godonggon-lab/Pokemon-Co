from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n255 255 255\n100\n', '1\r\n'),
        edge('2 2\n100 100 100 0 0 0\n200 200 200 10 10 10\n100\n', '1\r\n'),
        stress('3 3\n0 0 0 255 255 255 0 0 0\n255 255 255 255 255 255 0 0 0\n0 0 0 0 0 0 255 255 255\n100\n', '2\r\n'),
    ]
