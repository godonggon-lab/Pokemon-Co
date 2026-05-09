from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 1\n.\n", ".\n"),
        edge("1 1 2\n.\n", "O\n"),
        edge("1 1 3\nO\n", ".\n"),
        edge("2 2 1\nO.\n..\n", "O.\n..\n"),
        edge("2 2 2\nO.\n..\n", "OO\nOO\n"),
        stress("3 3 3\nO..\n...\n..O\n", "..O\n.O.\nO..\n"),
    ]
