from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n0\n', '0\r\n'),
        edge('1\n9\n', '9\r\n'),
        edge('5\n54321\n', '15\r\n'),
        edge('10\n0000000000\n', '0\r\n'),
        edge('10\n9090909090\n', '45\r\n'),
        stress('100\n1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890\n', '450\r\n'),
    ]
