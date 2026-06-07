from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\nX\n', '\r\n'),
        edge('3 3\nXXX\nXXX\nXXX\n', 'XXX\r\nXXX\r\nXXX\r\n'),
        edge('5 5\n.....\n.XXX.\n.XXX.\n.XXX.\n.....\n', 'XXX\r\nXXX\r\nXXX\r\n'),
        stress('8 8\n.X.X.X.X\nX.X.X.X.\n.X.X.X.X\nX.X.X.X.\n.X.X.X.X\nX.X.X.X.\n.X.X.X.X\nX.X.X.X.\n', '\r\n'),
    ]
