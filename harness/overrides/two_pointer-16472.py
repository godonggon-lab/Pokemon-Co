from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\naaaa\n', '4\r\n'),
        edge('2\nabcabc\n', '2\r\n'),
        stress('3\naabacbebebe\n', '7\r\n'),
    ]
