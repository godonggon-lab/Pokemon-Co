from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, q = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    queries = list(map(int, lines[2].split()))
    products = []
    for i in range(n):
        value = 1
        for j in range(4):
            value *= arr[(i + j) % n]
        products.append(value)
    score = sum(products)
    out = []
    for query in queries[:q]:
        idx = query - 1
        for start in range(idx - 3, idx + 1):
            pos = start % n
            score -= 2 * products[pos]
            products[pos] *= -1
        out.append(str(score))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "4 2\n1 2 3 4\n1 2\n",
        "5 3\n1 -1 1 -1 1\n1 3 5\n",
        "6 4\n1 2 3 4 5 6\n6 5 4 3\n",
        "4 1\n1 1 1 1\n1\n",
        "5 4\n0 1 0 1 0\n2 2 2 2\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    arr = " ".join(str((i % 5) - 2 or 1) for i in range(100))
    queries = " ".join(str(i % 100 + 1) for i in range(100))
    stdin = f"100 100\n{arr}\n{queries}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
