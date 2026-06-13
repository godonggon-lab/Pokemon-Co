from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('abc\nabc\n', '3\r\n'),
        edge('abc\ndef\n', '0\r\n'),
        edge('a\na\n', '1\r\n'),
        edge('a\nb\n', '0\r\n'),
        edge('banana\nananas\n', '5\r\n'),
        stress('ABRACADABRA\nECADADABRBCRDARA\n', '5\r\n'),
    ]
