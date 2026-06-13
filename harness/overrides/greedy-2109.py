from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('0\n', '0\r\n'),
        edge('3\n10 1\n20 1\n30 2\n', '50\r\n'),
        edge('1\n7 1\n', '7\r\n'),
        edge('3\n10 1\n20 1\n30 1\n', '30\r\n'),
        edge('4\n5 4\n10 3\n20 2\n40 1\n', '75\r\n'),
        stress('6\n50 2\n10 1\n20 2\n30 1\n40 3\n60 3\n', '150\r\n'),
    ]
