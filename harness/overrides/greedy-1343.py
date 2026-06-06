from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('XXXXXX\n', 'AAAABB\r\n'),
        edge('XX.XX\n', 'BB.BB\r\n'),
        edge('X\n', '-1\r\n'),
        edge('XXXX.XX.XXXXXX\n', 'AAAA.BB.AAAABB\r\n'),
        edge('....\n', '....\r\n'),
        stress('XXXXXXXXXX.XX.XXXX.XXXXXXXXXXXX\n', 'AAAAAAAABB.BB.AAAA.AAAAAAAAAAAA\r\n'),
    ]
