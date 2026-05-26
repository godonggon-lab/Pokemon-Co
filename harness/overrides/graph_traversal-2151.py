from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n#..\n...\n..#\n"),
        edge("5\n#.!..\n*.*..\n..!..\n..*.*\n..!#.\n"),
        stress("7\n#.!...!\n.*.*.*.\n..!....\n.*.*.*.\n....!..\n.*.*.*.\n!...!.#\n"),
    ]
