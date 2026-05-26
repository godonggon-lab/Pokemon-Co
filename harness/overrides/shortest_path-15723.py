from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\na is b\n2\na is b\nb is a\n"), stress("3\na is b\nb is c\nd is e\n4\na is c\nc is a\nd is e\na is e\n")]
