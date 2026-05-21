from __future__ import annotations

from functools import lru_cache
from typing import Dict, List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    m = int(lines[1])
    needs = [[] for _ in range(n + 1)]
    for line in lines[2 : 2 + m]:
        x, y, k = map(int, line.split())
        needs[x].append((y, k))

    @lru_cache(None)
    def calc(part: int) -> Dict[int, int]:
        if not needs[part]:
            return {part: 1}
        total: Dict[int, int] = {}
        for sub, count in needs[part]:
            for base, amount in calc(sub).items():
                total[base] = total.get(base, 0) + amount * count
        return total

    answer = calc(n)
    return "\n".join(f"{part} {answer[part]}" for part in sorted(answer))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "7\n8\n5 1 2\n5 2 2\n7 5 2\n6 5 3\n6 3 4\n7 6 3\n7 4 5\n5 3 1\n",
        "3\n1\n3 1 2\n",
        "4\n2\n4 2 3\n4 1 1\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
