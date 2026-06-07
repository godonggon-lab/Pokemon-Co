from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('0\n', '0'),
        edge('1\n', '1'),
        edge('7\n', '111'),
        edge('10\n', '1000'),
        edge('12345670\n', '1010011100101110111000'),
        stress('77777777777777777777\n', '111111111111111111111111111111111111111111111111111111111111'),
    ]
