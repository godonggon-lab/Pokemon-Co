from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    n, k = map(int, stdin.split())
    erased = [False] * (n + 1)
    for i in range(2, n + 1):
        if erased[i]:
            continue
        for j in range(i, n + 1, i):
            if not erased[j]:
                erased[j] = True
                k -= 1
                if k == 0:
                    return f"{j}\n"
    return ""


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["10 1\n", "10 3\n", "10 7\n", "20 10\n", "50 20\n", "100 50\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
