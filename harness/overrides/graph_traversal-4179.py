from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\nJ\n"),
        edge("1 2\nJ.\n"),
        edge("3 3\n###\n#J#\n###\n"),
        edge("3 3\n...\n.J.\n...\n"),
        edge("4 4\n####\n#JF#\n#..#\n#..#\n"),
        stress("5 6\n######\n#J...#\n#.##.#\n#...F#\n#....#\n"),
    ]
