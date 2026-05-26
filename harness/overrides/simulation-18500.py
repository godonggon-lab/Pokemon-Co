from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 6\n......\n..xx..\n..xx..\n..xx..\nxxxxxx\n1\n3\n"),
        edge("6 7\n.......\n..xxx..\n..x.x..\n..xxx..\n...x...\nxxxxxxx\n2\n2 4\n"),
        stress("7 8\n........\n...xx...\n..xxxx..\n...xx...\n..xxxx..\n...xx...\nxxxxxxxx\n3\n2 5 3\n"),
    ]
