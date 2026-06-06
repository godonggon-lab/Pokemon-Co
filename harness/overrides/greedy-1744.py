from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1\n', '1\r\n'),
        edge('3\n1\n2\n3\n', '7\r\n'),
        edge('5\n-1\n-2\n-3\n0\n4\n', '10\r\n'),
        edge('6\n-5\n-4\n-1\n0\n1\n2\n', '23\r\n'),
        edge('5\n-1\n2\n1\n1\n3\n', '7\r\n'),
        stress('20\n-4\n-3\n-2\n-1\n0\n1\n2\n3\n4\n-4\n-3\n-2\n-1\n0\n1\n2\n3\n4\n-4\n-3\n', '73\r\n'),
    ]
