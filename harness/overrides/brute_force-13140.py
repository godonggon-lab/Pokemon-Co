from __future__ import annotations

from itertools import permutations
from typing import List

from harness.cases import GeneratedCase, edge, stress


REPLACE_SAMPLES = True


def expected(stdin: str) -> str:
    target = int(stdin)
    letters = "helowrd"
    for perm in permutations(range(10), len(letters)):
        mp = dict(zip(letters, perm))
        if mp["h"] == 0 or mp["w"] == 0:
            continue
        hello = mp["h"] * 10000 + mp["e"] * 1000 + mp["l"] * 110 + mp["o"]
        world = mp["w"] * 10000 + mp["o"] * 1000 + mp["r"] * 100 + mp["l"] * 10 + mp["d"]
        if hello + world == target:
            return f"  {hello}\n+ {world}\n-------\n{target:7d}\n"
    return "No Answer\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["66971\n", "12345\n", "77777\n", "100000\n", "101520\n", "110000\n", "99999\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
