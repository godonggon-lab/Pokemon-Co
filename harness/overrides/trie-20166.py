from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 2 3\nAB\nCD\nA\nAB\nABA\n', '1\r\n2\r\n4\r\n'),
        stress('3 3 4\nABC\nDEF\nGHI\nADG\nAEI\nABC\nCFI\n', '1\r\n1\r\n1\r\n1\r\n'),
    ]
