from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('7 4\n3\n6\n7\n4\n', '0\r\n3\r\n3\r\n0\r\n'),
        edge('10 5\n2\n4\n8\n5\n10\n', '0\r\n2\r\n2\r\n2\r\n2\r\n'),
        stress('31 8\n16\n8\n24\n12\n30\n2\n3\n6\n', '0\r\n0\r\n0\r\n0\r\n0\r\n0\r\n0\r\n3\r\n'),
    ]
