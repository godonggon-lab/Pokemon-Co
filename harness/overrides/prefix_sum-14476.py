from __future__ import annotations

import math
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    prefix = [0] * (n + 1)
    suffix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = math.gcd(prefix[i], arr[i])
    for i in range(n - 1, -1, -1):
        suffix[i] = math.gcd(suffix[i + 1], arr[i])
    best = (-1, -1)
    for i in range(n):
        g = math.gcd(prefix[i], suffix[i + 1])
        if arr[i] % g != 0 and g > best[0]:
            best = (g, arr[i])
    return "-1" if best[0] == -1 else f"{best[0]} {best[1]}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["3\n6 10 15\n", "3\n2 4 8\n", "5\n12 15 18 27 30\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    arr = " ".join(str(6 * (i + 2)) for i in range(100)) + " 35"
    stdin = f"101\n{arr}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
