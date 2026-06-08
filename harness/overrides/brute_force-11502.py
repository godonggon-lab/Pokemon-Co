from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

SIEVE = [True] * 1001
SIEVE[0] = SIEVE[1] = False
for i in range(2, 32):
    if SIEVE[i]:
        for j in range(i * i, 1001, i):
            SIEVE[j] = False
PRIMES = [i for i in range(2, 1001) if SIEVE[i]]

def _solve(data: str) -> str:
    lines = data.splitlines()
    out = []
    for line in lines[1:1 + int(lines[0])]:
        k = int(line)
        found = None
        for a in PRIMES:
            if found:
                break
            for b in PRIMES:
                c = k - a - b
                if 2 <= c <= 1000 and SIEVE[c]:
                    found = f"{a} {b} {c}"
                    break
        out.append(found or "0")
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n7\n"),
        edge("1\n6\n"),
        edge("2\n8\n10\n"),
        edge("3\n11\n25\n999\n"),
        edge("3\n17\n31\n997\n"),
        stress("5\n33\n99\n123\n777\n1000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
