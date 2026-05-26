from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n"), edge("2 4\n"), stress("4 10\n")]
