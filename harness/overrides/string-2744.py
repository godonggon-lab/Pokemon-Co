from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('a\n', 'A\r\n'),
        edge('Z\n', 'z\r\n'),
        edge('HelloWorld\n', 'hELLOwORLD\r\n'),
        edge('BaEkJoOn\n', 'bAeKjOoN\r\n'),
        edge('abcXYZ\n', 'ABCxyz\r\n'),
        stress('DongJunCodeDex\n', 'dONGjUNcODEdEX\r\n'),
    ]
