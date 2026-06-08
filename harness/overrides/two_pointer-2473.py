from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n-1 0 2\n', '-1 0 2\r\n'),
        edge('5\n-5 -2 -1 4 10\n', '-2 -1 4\r\n'),
        edge('5\n-100 -10 1 2 98\n', '-100 2 98\r\n'),
        edge('6\n-9 -4 -1 3 7 11\n', '-9 3 7\r\n'),
        edge('5\n1 2 3 4 5\n', '1 2 3\r\n'),
        stress('30\n-100 -93 -86 -79 -72 -65 -58 -51 -44 -37 -30 -23 -16 -9 -2 5 12 19 26 33 40 47 54 61 68 75 82 89 96 103\n', '-9 -2 12\r\n'),
    ]
