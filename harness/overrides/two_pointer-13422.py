from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    t = int(lines[0])
    idx = 1
    out = []
    for _ in range(t):
        n, m, k = map(int, lines[idx].split())
        idx += 1
        arr = list(map(int, lines[idx].split()))
        idx += 1
        if n == m:
            out.append(str(1 if sum(arr) < k else 0))
            continue
        doubled = arr + arr
        window = sum(arr[:m])
        answer = 1 if window < k else 0
        for i in range(1, n):
            window += doubled[i + m - 1] - doubled[i - 1]
            answer += int(window < k)
        out.append(str(answer))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n5 3 10\n1 2 3 4 5\n",
        "1\n3 3 7\n1 2 3\n",
        "2\n4 2 5\n2 2 2 2\n4 4 10\n1 2 3 4\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    arr = " ".join(str(i % 10 + 1) for i in range(1000))
    stdin = f"1\n1000 50 300\n{arr}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
