from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    value, base_text = stdin.split()
    base = int(base_text)
    result = 0
    for ch in value:
        result = result * base + (int(ch) if ch.isdigit() else ord(ch) - 55)
    return f"{result}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["10 10\n", "1010 2\n", "FF 16\n", "ZZ 36\n", "ABC 16\n", "HELLO 36\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
