from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    answer = 0
    while any(arr):
        for i in range(n):
            if arr[i] % 2:
                arr[i] -= 1
                answer += 1
        if any(arr):
            arr = [x // 2 for x in arr]
            answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n0\n", "1\n1\n", "3\n2 4 8\n", "3\n1 2 3\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "100\n" + " ".join(str(i * 12345 % 100000) for i in range(100)) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
