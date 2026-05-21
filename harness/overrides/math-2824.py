from __future__ import annotations

import math
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    a = list(map(int, lines[1].split()))
    m = int(lines[2])
    b = list(map(int, lines[3].split()))
    answer = 1
    trimmed = False
    for i in range(n):
        x = a[i]
        for j in range(m):
            g = math.gcd(x, b[j])
            if g > 1:
                answer *= g
                if answer >= 1_000_000_000:
                    trimmed = True
                    answer %= 1_000_000_000
                x //= g
                b[j] //= g
            if x == 1:
                break
    return f"{answer:09d}" if trimmed else str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2\n2 3\n2\n4 5\n",
        "3\n2 4 8\n2\n16 32\n",
        "1\n99991\n1\n99991\n",
        "3\n1000000000 999999937 2\n2\n999999937 500000000\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "5\n" + " ".join(["720720"] * 5) + "\n5\n" + " ".join(["360360"] * 5) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
