from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    arr = sorted(map(int, lines[1].split()))
    prefix = [0]
    for value in arr:
        prefix.append(prefix[-1] + value)
    out = []
    for line in lines[2:]:
        l, r = map(int, line.split())
        out.append(str(prefix[r] - prefix[l - 1]))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["5 3\n5 4 3 2 1\n1 3\n2 5\n4 4\n", "1 1\n7\n1 1\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    arr = " ".join(str(1000 - i) for i in range(1000))
    queries = "\n".join(f"{i} {1000 - i}" for i in range(1, 500, 10))
    stdin = f"1000 50\n{arr}\n{queries}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
