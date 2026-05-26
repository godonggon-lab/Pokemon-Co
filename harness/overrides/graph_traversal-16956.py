from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 2\nSW\n"),
        edge("2 2\nS.\n.W\n"),
        stress("4 5\nS...W\n.....\n..S..\nW....\n"),
    ]
