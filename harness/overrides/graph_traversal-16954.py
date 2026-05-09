from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


EMPTY = "........\n" * 8


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge(EMPTY),
        edge("........\n........\n........\n........\n........\n........\n........\n#.......\n"),
        edge("........\n........\n........\n........\n........\n........\n#.......\n........\n"),
        edge("########\n........\n........\n........\n........\n........\n........\n........\n"),
        edge("........\n........\n........\n........\n........\n........\n........\n#######.\n"),
        stress("........\n........\n........\n........\n....#...\n...#....\n..#.....\n.#......\n"),
    ]
