from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n = int(stdin)
    prime = [True] * (n + 1)
    if n >= 0:
        prime[0] = False
    if n >= 1:
        prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    def happy(value: int) -> bool:
        seen = set()
        while value != 1 and value not in seen:
            seen.add(value)
            value = sum(int(ch) ** 2 for ch in str(value))
        return value == 1

    return "\n".join(str(i) for i in range(2, n + 1) if prime[i] and happy(i))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "10\n", "100\n", "2\n", "50\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("10000\n", _solve("10000\n")))
    return cases
