from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\nA B C\n2\nA B\nB C\n"),
        edge("5\nkim lee park choi jung\n3\nlee kim\npark kim\nchoi lee\n"),
        stress("6\na b c d e f\n5\nb a\nc a\nd b\ne b\nf c\n"),
    ]
