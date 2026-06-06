from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n10\n', '10\r\n'),
        edge('2\n10\n20\n', '30\r\n'),
        edge('3\n10\n20\n30\n', '50\r\n'),
        edge('4\n10\n20\n30\n40\n', '80\r\n'),
        edge('6\n1\n2\n3\n4\n5\n6\n', '16\r\n'),
        stress('10\n10\n10\n9\n9\n8\n8\n7\n7\n6\n6\n', '57\r\n'),
    ]
