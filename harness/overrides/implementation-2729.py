from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n0 0\n', '0\r\n'),
        edge('1\n1 1\n', '10\r\n'),
        edge('2\n10 1\n101 11\n', '11\r\n1000\r\n'),
        edge('3\n1111 1\n1010 1010\n100000 1\n', '10000\r\n10100\r\n100001\r\n'),
        edge('4\n0 1\n1 0\n111 111\n1001 1011\n', '1\r\n1\r\n1110\r\n10100\r\n'),
        stress('5\n101010 010101\n111111 1\n1000000 1000000\n1010101010 11110000\n1 1111111111\n', '111111\r\n1000000\r\n10000000\r\n1110011010\r\n10000000000\r\n'),
    ]
