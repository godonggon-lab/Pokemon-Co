from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('A\n', "I'm a winner!\r\n"),
        edge('B\n', "You're the winner?\r\n"),
        edge('ABC\n', "You're the winner?\r\n"),
        edge('HELLO\n', "I'm a winner!\r\n"),
        edge('DONGJUN\n', "You're the winner?\r\n"),
        stress('CODEDEX\n', "You're the winner?\r\n"),
    ]
