from __future__ import annotations

from collections import defaultdict
from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    idx = 1
    out = []
    for _ in range(int(lines[0])):
        word = lines[idx]
        k = int(lines[idx + 1])
        idx += 2
        positions: dict[str, list[int]] = defaultdict(list)
        for i, ch in enumerate(word):
            positions[ch].append(i)
        shortest = 10**9
        longest = 0
        for pos in positions.values():
            for i in range(len(pos) - k + 1):
                length = pos[i + k - 1] - pos[i] + 1
                shortest = min(shortest, length)
                longest = max(longest, length)
        out.append("-1" if longest == 0 else f"{shortest} {longest}")
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\nabc\n1\n", "1\nabc\n2\n", "1\nabaaaba\n3\n", "2\nsuperaquatornado\n2\nabcdefghijklmnopqrstuvwxyz\n1\n", "2\naaaaa\n2\nabacaba\n2\n", "3\nabcabcabc\n3\nzzzzzz\n4\naabbcc\n2\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
