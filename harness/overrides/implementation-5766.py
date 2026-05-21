from __future__ import annotations

from collections import Counter
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    tokens = iter(stdin.split())
    out: list[str] = []
    for n_s in tokens:
        n = int(n_s)
        m = int(next(tokens))
        if n == 0 and m == 0:
            break
        scores = [int(next(tokens)) for _ in range(n * m)]
        counter = Counter(scores)
        first = max(counter.values())
        second = max(v for v in counter.values() if v < first)
        out.append(" ".join(map(str, sorted(k for k, v in counter.items() if v == second))))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2 3\n1 2 3\n2 3 4\n0 0\n",
        "3 2\n1 1\n2 2\n3 4\n0 0\n",
        "2 3\n5 5 4\n3 2 1\n0 0\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    block = "5 5\n" + "\n".join(" ".join(str((i + j) % 8 + 1) for j in range(5)) for i in range(5)) + "\n0 0\n"
    cases.append(stress(block, _solve(block)))
    return cases
