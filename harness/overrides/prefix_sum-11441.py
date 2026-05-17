from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    data = list(map(int, stdin.split()))
    idx = 0
    n = data[idx]
    idx += 1
    arr = data[idx:idx + n]
    idx += n
    prefix = [0]
    for value in arr:
        prefix.append(prefix[-1] + value)

    m = data[idx]
    idx += 1
    out: list[str] = []
    for _ in range(m):
        left, right = data[idx], data[idx + 1]
        idx += 2
        out.append(str(prefix[right] - prefix[left - 1]))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n7\n3\n1 1\n1 1\n1 1\n",
        "5\n1 2 3 4 5\n4\n1 5\n2 4\n3 3\n5 5\n",
        "4\n-1 -2 -3 -4\n3\n1 4\n2 3\n4 4\n",
        "6\n10 -5 0 7 -2 3\n5\n1 1\n1 2\n2 5\n3 6\n6 6\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]

    n = 1000
    arr = [(i % 31) - 15 for i in range(1, n + 1)]
    queries = [(1, n), (500, 500), (100, 900), (2, 999), (123, 456)]
    stdin = (
        f"{n}\n"
        + " ".join(map(str, arr))
        + f"\n{len(queries)}\n"
        + "\n".join(f"{a} {b}" for a, b in queries)
        + "\n"
    )
    cases.append(stress(stdin, _solve(stdin)))
    return cases
