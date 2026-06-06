from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n0 0\n', '0\r\n'),
        edge('2\n0 0\n10 10\n', '20\r\n'),
        edge('3\n-1 -1\n0 0\n1 1\n', '4\r\n'),
        edge('5\n1 10\n2 20\n3 30\n4 40\n5 50\n', '66\r\n'),
        edge('4\n100 -100\n-100 100\n100 100\n-100 -100\n', '800\r\n'),
        stress('30\n-15 -8\n-14 -7\n-13 -4\n-12 1\n-11 8\n-10 0\n-9 -6\n-8 7\n-7 5\n-6 5\n-5 7\n-4 -6\n-3 0\n-2 8\n-1 1\n0 -4\n1 -7\n2 -8\n3 -7\n4 -4\n5 1\n6 8\n7 0\n8 -6\n9 7\n10 5\n11 5\n12 7\n13 -6\n14 0\n', '373\r\n'),
    ]
