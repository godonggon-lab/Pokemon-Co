from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 1\nC.C\n', '0\r\n'),
        edge('3 3\nC..\n.*.\n..C\n', '1\r\n'),
        stress('5 5\nC...*\n***.*\n....*\n.****\n....C\n', '4\r\n'),
    ]
