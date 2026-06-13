from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    t = int(lines[0])
    idx = 1
    out = []
    for _ in range(t):
        d, n = map(int, lines[idx].split())
        idx += 1
        arr = list(map(int, lines[idx].split()))
        idx += 1
        counts = [0] * d
        counts[0] = 1
        prefix = 0
        answer = 0
        for value in arr:
            prefix = (prefix + value) % d
            answer += counts[prefix]
            counts[prefix] += 1
        out.append(str(answer))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n3 5\n1 2 3 4 5\n",
        "2\n5 3\n5 5 5\n2 4\n1 1 1 1\n",
        "1\n7 1\n7\n",
        "1\n2 5\n1 1 1 1 1\n",
        "1\n10 4\n0 0 0 0\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    arr = " ".join(str(i % 97) for i in range(1000))
    stdin = f"1\n97 1000\n{arr}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
