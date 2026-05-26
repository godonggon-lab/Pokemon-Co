from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2\nmain a 1\nmain f1 0\na f2 0\na b 1\n2\nmain\na\n"),
        edge("3 3\nmain src 1\nsrc app 1\nsrc util 1\napp page 0\nutil db 0\nmain readme 0\n3\nmain\nmain/src\nmain/src/app\n"),
        stress("4 4\nmain A 1\nmain B 1\nA x 0\nA y 0\nB y 0\nB C 1\nC z 0\nC x 0\n2\nmain\nmain/B\n"),
    ]
