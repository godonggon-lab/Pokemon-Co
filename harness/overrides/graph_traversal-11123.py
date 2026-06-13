from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1 1\n#\n', '1\r\n'),
        edge('1\n3 3\n#.#\n.#.\n#.#\n', '5\r\n'),
        edge('1\n2 2\n..\n..\n', '0\r\n'),
        edge('1\n2 3\n###\n###\n', '1\r\n'),
        edge('2\n2 2\n#.\n.#\n3 1\n#\n.\n#\n', '2\r\n2\r\n'),
        stress('2\n5 5\n#####\n#...#\n#.#.#\n#...#\n#####\n4 4\n....\n....\n....\n....\n', '2\r\n0\r\n'),
    ]
