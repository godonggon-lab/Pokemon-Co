from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2\n5\n7\n', '5\r\n'),
        edge('4\n1\n2\n3\n4\n', '5\r\n'),
        stress('6\n8\n3\n5\n7\n2\n9\n', '17\r\n'),
    ]
