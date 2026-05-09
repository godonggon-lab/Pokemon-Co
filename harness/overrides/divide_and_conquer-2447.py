from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    n = int(stdin)

    def star(y: int, x: int) -> str:
        while y or x:
            if y % 3 == 1 and x % 3 == 1:
                return " "
            y //= 3
            x //= 3
        return "*"

    return "\n".join("".join(star(i, j) for j in range(n)) for i in range(n)) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["3\n", "9\n", "27\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
