from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 5\n#####\n#..B#\n#.#.#\n#RO.#\n#####\n"),
        edge("5 5\n#####\n#RBO#\n#...#\n#...#\n#####\n"),
        stress("7 7\n#######\n#...RB#\n#.#####\n#.....#\n#####.#\n#O....#\n#######\n"),
    ]
