from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2\n1\n1 2 5\n', '0 5\r\n0 0\r\n'),
        edge('5\n8\n1 2 2\n1 3 3\n2 3 1\n2 4 5\n3 4 1\n4 5 2\n1 5 20\n3 5 10\n', '0 2 3 4 6\r\n0 0 1 2 4\r\n0 0 0 1 3\r\n0 0 0 0 2\r\n0 0 0 0 0\r\n'),
        stress('10\n9\n1 2 1\n2 3 2\n3 4 3\n4 5 4\n5 6 5\n6 7 6\n7 8 7\n8 9 8\n9 10 9\n', '0 1 3 6 10 15 21 28 36 45\r\n0 0 2 5 9 14 20 27 35 44\r\n0 0 0 3 7 12 18 25 33 42\r\n0 0 0 0 4 9 15 22 30 39\r\n0 0 0 0 0 5 11 18 26 35\r\n0 0 0 0 0 0 6 13 21 30\r\n0 0 0 0 0 0 0 7 15 24\r\n0 0 0 0 0 0 0 0 8 17\r\n0 0 0 0 0 0 0 0 0 9\r\n0 0 0 0 0 0 0 0 0 0\r\n'),
    ]
