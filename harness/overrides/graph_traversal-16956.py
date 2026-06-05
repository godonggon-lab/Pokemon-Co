from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 2\nSW\n', '0\r\n'),
        edge('2 2\nS.\n.W\n', '1\r\nSD\r\nDW\r\n'),
        stress('4 5\nS...W\n.....\n..S..\nW....\n', '1\r\nSDDDW\r\nDDDDD\r\nDDSDD\r\nWDDDD\r\n'),
    ]
