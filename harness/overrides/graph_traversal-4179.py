from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\nJ\n', '1\r\n'),
        edge('1 2\nJ.\n', '1\r\n'),
        edge('3 3\n###\n#J#\n###\n', 'IMPOSSIBLE\r\n'),
        edge('3 3\n...\n.J.\n...\n', '2\r\n'),
        edge('4 4\n####\n#JF#\n#..#\n#..#\n', '3\r\n'),
        stress('5 6\n######\n#J...#\n#.##.#\n#...F#\n#....#\n', '4\r\n'),
    ]
