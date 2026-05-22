from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\nk\n"), edge("3 3\n...\n.kv\n...\n"), edge("4 5\n####.\n#kv#.\n#kk#v\n.....\n"), stress("10 10\n" + "\n".join(("kv." * 4)[:10] if i % 2 else ("..#kv#.." * 2)[:10] for i in range(10)) + "\n")]
