from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('a\na\n', '1\r\n'),
        edge('ab\nabab\n', '1\r\n'),
        edge('ab\naba\n', '0\r\n'),
        edge('abc\nabcabc\n', '1\r\n'),
        edge('abab\nab\n', '1\r\n'),
        stress('abcab\nabc\n', '0\r\n'),
    ]
