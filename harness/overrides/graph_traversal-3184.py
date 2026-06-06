from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\no\n', '1 0\r\n'),
        edge('3 3\n...\n.ov\n...\n', '0 1\r\n'),
        edge('6 6\n...#..\n.##v#.\n#v.#.#\n#.o#.#\n.###.#\n...###\n', '0 2\r\n'),
        stress('10 10\n..#ov#....\nov.ov.ov.o\n..#ov#....\nov.ov.ov.o\n..#ov#....\nov.ov.ov.o\n..#ov#....\nov.ov.ov.o\n..#ov#....\nov.ov.ov.o\n', '25 0\r\n'),
    ]
