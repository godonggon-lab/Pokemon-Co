from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, t = map(int, lines[0].split())
    items = [tuple(map(int, line.split())) for line in lines[1 : 1 + n]]
    items.sort(key=lambda item: item[1])
    start = t - n
    return str(sum(w + p * (start + i) for i, (w, p) in enumerate(items)))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3 5\n1 3\n2 2\n3 1\n",
        "1 10\n5 7\n",
        "4 4\n10 1\n10 2\n10 3\n10 4\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    rows = "\n".join(f"{i} {101 - i}" for i in range(1, 101))
    stdin = f"100 1000\n{rows}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
