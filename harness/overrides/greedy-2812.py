from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n12\n', '2\r\n'),
        edge('4 2\n1924\n', '94\r\n'),
        edge('6 3\n123123\n', '323\r\n'),
        edge('10 4\n4177252841\n', '775841\r\n'),
        edge('5 2\n99999\n', '999\r\n'),
        stress('12 6\n987654321234\n', '987654\r\n'),
    ]
