from __future__ import annotations

import itertools
from typing import List

from harness.cases import GeneratedCase, edge


def _solve(stdin: str) -> str:
    k, m = map(int, stdin.split())
    limit = 10**k
    prime = [True] * limit
    prime[0] = False
    prime[1] = False
    for i in range(2, int((limit - 1) ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, limit, i):
                prime[j] = False
    primes = [i for i in range(2, limit) if prime[i]]
    sum_ok = [False] * limit
    for i, a in enumerate(primes):
        for b in primes[i + 1 :]:
            value = a + b
            if value >= limit:
                break
            sum_ok[value] = True
    mul_ok = [False] * limit
    for i, a in enumerate(primes):
        if a * a >= limit:
            break
        for b in primes[i:]:
            value = a * b
            if value >= limit:
                break
            mul_ok[value] = True
    answer = 0
    for perm in itertools.permutations("0123456789", k):
        if perm[0] == "0":
            continue
        value = int("".join(perm))
        reduced = value
        while reduced % m == 0:
            reduced //= m
        if sum_ok[value] and mul_ok[reduced]:
            answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1 2\n", "2 2\n", "3 3\n"]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
