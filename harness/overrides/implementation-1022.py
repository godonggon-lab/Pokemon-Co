from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _value(r: int, c: int) -> int:
    layer = max(abs(r), abs(c))
    end = (2 * layer + 1) ** 2
    if r == layer:
        return end - (layer - c)
    end -= 2 * layer
    if c == -layer:
        return end - (layer - r)
    end -= 2 * layer
    if r == -layer:
        return end - (c + layer)
    end -= 2 * layer
    return end - (r + layer)


def _solve(stdin: str) -> str:
    r1, c1, r2, c2 = map(int, stdin.split())
    grid = [[_value(r, c) for c in range(c1, c2 + 1)] for r in range(r1, r2 + 1)]
    width = max(len(str(item)) for row in grid for item in row)
    return "\n".join(" ".join(str(item).rjust(width) for item in row) for row in grid)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["0 0 0 0\n", "-1 -1 1 1\n", "-3 -2 2 3\n", "1 1 1 3\n", "-2 0 0 0\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("-50 -50 49 49\n", _solve("-50 -50 49 49\n")))
    return cases
