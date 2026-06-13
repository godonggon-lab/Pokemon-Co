from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('5 2 1\n', '0.7\r\n'),
        edge('10 3 2\n', '0.18333333333333332\r\n'),
        edge('5 2 0\n', '1.0\r\n'),
        edge('5 5 5\n', '1.0\r\n'),
        edge('5 1 1\n', '0.2\r\n'),
        stress('20 10 5\n', '0.6718591006516703\r\n'),
    ]
