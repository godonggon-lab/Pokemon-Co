from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    loss = list(map(int, lines[1].split()))
    joy = list(map(int, lines[2].split()))
    dp = [0] * 100
    for hp_loss, hp_joy in zip(loss[:n], joy[:n]):
        for hp in range(99, hp_loss - 1, -1):
            dp[hp] = max(dp[hp], dp[hp - hp_loss] + hp_joy)
    return str(max(dp))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n99\n100\n"),
        edge("1\n100\n1000\n"),
        edge("3\n1 21 79\n20 30 25\n"),
        edge("4\n25 25 25 25\n10 20 30 40\n"),
        edge("5\n1 1 1 1 1\n1 2 3 4 5\n"),
        stress("5\n10 20 30 40 50\n5 20 30 40 100\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
