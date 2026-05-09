from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("A\n"),
        edge("B\n"),
        edge("ABC\n"),
        edge("HELLO\n"),
        edge("DONGJUN\n"),
        stress("CODEDEX\n"),
    ]
