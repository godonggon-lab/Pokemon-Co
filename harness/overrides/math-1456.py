from __future__ import annotations

import math
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    a, b = map(int, stdin.split())
    limit = math.isqrt(b)
    is_prime = [True] * (limit + 1)
    if limit >= 1:
        is_prime[0] = False
        is_prime[1] = False
    elif limit == 0:
        is_prime[0] = False
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    answer = 0
    for p in range(2, limit + 1):
        if not is_prime[p]:
            continue
        value = p * p
        while value <= b:
            if value >= a:
                answer += 1
            if value > b // p:
                break
            value *= p
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1 10\n",
        "4 4\n",
        "8 24\n",
        "100 1000\n",
        "999 10000\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("1 1000000\n", _solve("1 1000000\n")))
    return cases
