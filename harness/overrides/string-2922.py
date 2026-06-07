from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('L\n', '1\r\n'),
        edge('_\n', '1\r\n'),
        stress('L__A_E\n', '4410\r\n'),
    ]
