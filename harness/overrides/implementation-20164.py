from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def _solve(stdin: str) -> str:
    s = stdin.strip()
    mn = 10**9
    mx = 0

    def odd_count(value: str) -> int:
        return sum((ord(ch) - 48) % 2 for ch in value)

    def dfs(value: str, total: int) -> None:
        nonlocal mn, mx
        total += odd_count(value)
        if len(value) == 1:
            mn = min(mn, total)
            mx = max(mx, total)
        elif len(value) == 2:
            dfs(str(int(value[0]) + int(value[1])), total)
        else:
            for i in range(1, len(value) - 1):
                for j in range(i + 1, len(value)):
                    dfs(str(int(value[:i]) + int(value[i:j]) + int(value[j:])), total)

    dfs(s, 0)
    return f"{mn} {mx}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "12\n", "82019\n", "999999\n"]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
