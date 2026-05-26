from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("M\n"), edge("MKM\n"), stress("MMKMMMKMMMM\n")]
