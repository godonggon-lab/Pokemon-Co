from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n', '-1\r\n'),
        edge('3\n', '2\r\n'),
        edge('15\n', '4\r\n8\r\n'),
        edge('100\n', '26\r\n'),
        stress('99999\n', '320\r\n468\r\n1240\r\n5560\r\n16668\r\n50000\r\n'),
    ]
