from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1 1\n@\n', '1\r\n'),
        edge('1\n3 3\n###\n#@#\n###\n', 'IMPOSSIBLE\r\n'),
        edge('1\n3 3\n...\n.@.\n...\n', '2\r\n'),
        edge('1\n4 4\n####\n#@.#\n#..#\n#*.#\n', 'IMPOSSIBLE\r\n'),
        edge('1\n5 4\n.....\n.###.\n.@*#.\n.....\n', '2\r\n'),
        stress('2\n4 3\n@..#\n.*.#\n....\n5 4\n#####\n#@..#\n#.*.#\n#####\n', '1\r\nIMPOSSIBLE\r\n'),
    ]
