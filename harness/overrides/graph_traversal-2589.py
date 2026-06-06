from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\nL\n', '0\r\n'),
        edge('1 3\nLLL\n', '2\r\n'),
        edge('2 2\nLL\nLL\n', '2\r\n'),
        edge('3 3\nLLL\nWWW\nLLL\n', '2\r\n'),
        edge('5 7\nWLLWWWL\nLLLWLLL\nLWLWLWW\nLWLWLLL\nWLLWLWW\n', '8\r\n'),
        stress('8 8\nLLLLLLLL\nLWWWWWLL\nLLLLLWLL\nLLWWWLLL\nLLLLLLLL\nLWWWWWWL\nLLLLLLLL\nWWWWLLLW\n', '15\r\n'),
    ]
