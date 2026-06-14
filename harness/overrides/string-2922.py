from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('L\n', '1\r\n'),
        edge('_\n', '1\r\n'),
        edge('A\n', '0\r\n'),
        edge('___\n', '690\r\n'),
        edge('L_A\n', '26\r\n'),
        stress('L__A_E\n', '4410\r\n'),
    ]
