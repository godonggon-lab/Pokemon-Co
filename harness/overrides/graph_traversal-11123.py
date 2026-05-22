from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1 1\n#\n"), edge("1\n3 3\n#.#\n.#.\n#.#\n"), stress("2\n5 5\n#####\n#...#\n#.#.#\n#...#\n#####\n4 4\n....\n....\n....\n....\n")]
