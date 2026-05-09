from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    groups = stdin.strip().split("-")
    first = sum(map(int, groups[0].split("+")))
    rest = sum(sum(map(int, group.split("+"))) for group in groups[1:])
    return f"{first - rest}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "1+2+3\n", "10-5\n", "55-50+40\n", "10+20-30+40-50\n", "00009-00009+00001\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
