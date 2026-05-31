from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    k = int(lines[0])
    values = list(map(int, lines[1].split()))
    levels: list[list[int]] = [[] for _ in range(k)]

    def build(start: int, end: int, depth: int) -> None:
        if start > end:
            return
        mid = (start + end) // 2
        levels[depth].append(values[mid])
        build(start, mid - 1, depth + 1)
        build(mid + 1, end, depth + 1)

    build(0, len(values) - 1, 0)
    return "\n".join(" ".join(map(str, level)) for level in levels)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n1\n",
        "2\n1 2 3\n",
        "3\n1 6 4 3 5 2 7\n",
        "4\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    hard = "5\n" + " ".join(str(i) for i in range(1, 32)) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
