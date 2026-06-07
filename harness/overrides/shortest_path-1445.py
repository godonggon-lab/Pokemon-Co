from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 2\nSF\n..\n', '0 0\r\n'),
        edge('3 3\nSg.\n...\n..F\n', '0 0\r\n'),
        stress('5 5\nS....\n.gg..\n..g..\n...g.\n....F\n', '0 2\r\n'),
    ]
