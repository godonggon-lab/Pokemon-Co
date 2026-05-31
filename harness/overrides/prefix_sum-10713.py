from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    route = list(map(int, lines[1].split()))
    diff = [0] * (n + 1)
    for a, b in zip(route, route[1:]):
        if a > b:
            a, b = b, a
        diff[a] += 1
        diff[b] -= 1
    count = 0
    answer = 0
    for i, line in enumerate(lines[2 : 2 + n - 1], 1):
        count += diff[i]
        a, b, c = map(int, line.split())
        answer += min(count * a, count * b + c)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "4 4\n1 2 4 3\n10 1 5\n10 1 5\n10 1 5\n",
        "2 2\n1 2\n3 2 10\n",
        "5 5\n5 1 3 2 4\n1 1 100\n2 1 1\n3 2 1\n4 1 20\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    n = 20
    route = [1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15]
    costs = [f"{i + 2} {i % 5 + 1} {i * 3}" for i in range(1, n)]
    hard = f"{n} {len(route)}\n" + " ".join(map(str, route)) + "\n" + "\n".join(costs) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
