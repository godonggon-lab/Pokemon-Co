from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('K\n', '0\r\n'),
        edge('R\n', '1\r\n'),
        edge('KKKK\n', '0\r\n'),
        edge('RRRR\n', '4\r\n'),
        edge('KKRRKK\n', '6\r\n'),
        stress('KKRKRKRRKKR\n', '8\r\n'),
    ]
