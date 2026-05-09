from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    source, target = stdin.split()
    source = "".join(ch for ch in source if not ch.isdigit())
    return ("1" if target in source else "0") + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["a1b2c3\nabc\n", "a1b2c3\nac\n", "123abc456\nabc\n", "1a2b3c\nabcd\n", "hello123world\nlow\n", "d0o1n2g3j4u5n\ndongjun\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
