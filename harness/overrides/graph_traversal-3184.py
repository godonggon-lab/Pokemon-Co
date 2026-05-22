from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\no\n"), edge("3 3\n...\n.ov\n...\n"), edge("6 6\n...#..\n.##v#.\n#v.#.#\n#.o#.#\n.###.#\n...###\n"), stress("10 10\n" + "\n".join(("ov." * 4)[:10] if i % 2 else ("..#ov#.." * 2)[:10] for i in range(10)) + "\n")]
