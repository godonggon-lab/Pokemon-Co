from __future__ import annotations

import random
from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def _solve(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n, m = nums[0], nums[1]
    cards = nums[2 : 2 + n]
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                total = cards[i] + cards[j] + cards[k]
                if total <= m:
                    best = max(best, total)
    return f"{best}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases: List[GeneratedCase] = []
    inputs = [
        "5 21\n5 6 7 8 9\n",
        "10 500\n93 181 245 214 315 36 185 138 216 295\n",
        "3 5\n1 2 3\n",
    ]
    cases.extend(fuzz(stdin) for stdin in inputs[:2])
    cases.append(edge(inputs[2], _solve(inputs[2])))
    for i in range(3):
        rng = random.Random(f"2798:{i}")
        n = rng.randint(3, 12)
        m = rng.randint(20, 300)
        arr = [rng.randint(1, 100) for _ in range(n)]
        stdin = f"{n} {m}\n" + " ".join(map(str, arr)) + "\n"
        cases.append(edge(stdin, _solve(stdin)))
    stdin = "20 1000\n" + " ".join(str(i * 17 % 400 + 1) for i in range(20)) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
