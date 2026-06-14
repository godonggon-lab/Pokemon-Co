from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\naaaa\n', '4\r\n'),
        edge('2\nabcabc\n', '2\r\n'),
        edge('1\nz\n', '1\r\n'),
        edge('5\nabcde\n', '5\r\n'),
        edge('2\nabababab\n', '8\r\n'),
        stress('3\naabacbebebe\n', '7\r\n'),
    ]
