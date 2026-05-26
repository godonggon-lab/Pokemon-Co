from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("SSSSS\nSSSSS\nSSSSS\nSSSSS\nSSSSS\n"),
        edge("YYYYY\nYYYYY\nYYYYY\nYYYYY\nYYYYY\n"),
        stress("SYSYS\nYSYSY\nSYSYS\nYSYSY\nSYSYS\n"),
    ]
