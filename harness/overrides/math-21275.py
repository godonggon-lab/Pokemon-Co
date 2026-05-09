from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def convert(value: str, base: int) -> int | None:
    result = 0
    for ch in value:
        digit = int(ch) if ch.isdigit() else ord(ch) - 87
        if digit >= base:
            return None
        result = result * base + digit
        if result > 2**63 - 1:
            return None
    return result


def expected(stdin: str) -> str:
    a, b = stdin.split()
    answers = []
    for base_a in range(2, 37):
        va = convert(a, base_a)
        if va is None:
            continue
        for base_b in range(2, 37):
            if base_a == base_b:
                continue
            if convert(b, base_b) == va:
                answers.append((va, base_a, base_b))
    if not answers:
        return "Impossible\n"
    if len(answers) > 1:
        return "Multiple\n"
    return f"{answers[0][0]} {answers[0][1]} {answers[0][2]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1 1\n", "10 2\n", "a 10\n", "z 35\n", "101 5\n", "abc 123\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
