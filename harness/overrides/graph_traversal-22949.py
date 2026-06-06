from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\nS...\n....\n....\n...E\n', '6\r\n'),
        edge('1\nS#..\n.#..\n..#.\n...E\n', '6\r\n'),
        stress('1\nS...\n.##.\n....\n...E\n', '6\r\n'),
    ]
