from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress

ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
POS = {ch: (r, c) for r, row in enumerate(ROWS) for c, ch in enumerate(row)}
LEFT = set("qwertasdfgzxcv")


def expected(stdin: str) -> str:
    first, word = stdin.splitlines()
    left, right = first.split()
    total = 0
    for ch in word:
        hand = left if ch in LEFT else right
        total += abs(POS[hand][0] - POS[ch][0]) + abs(POS[hand][1] - POS[ch][1]) + 1
        if ch in LEFT:
            left = ch
        else:
            right = ch
    return f"{total}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["q p\nqwerty\n", "q p\nplmokn\n", "a l\nasdfjkl\n", "z m\nzzzzmmmm\n", "f j\ndongjun\n", "q p\nabcdefghijklmnopqrstuvwxyz\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
