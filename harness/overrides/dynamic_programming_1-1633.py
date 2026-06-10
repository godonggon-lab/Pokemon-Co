from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    players = [tuple(map(int, line.split())) for line in data.splitlines() if line.strip()]
    dp = [[-1] * 16 for _ in range(16)]
    dp[0][0] = 0
    for white, black in players:
        nxt = [row[:] for row in dp]
        for w in range(16):
            for b in range(16):
                if dp[w][b] < 0:
                    continue
                if w < 15:
                    nxt[w + 1][b] = max(nxt[w + 1][b], dp[w][b] + white)
                if b < 15:
                    nxt[w][b + 1] = max(nxt[w][b + 1], dp[w][b] + black)
        dp = nxt
    return f"{dp[15][15]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    base = "\n".join(f"{i} {31-i}" for i in range(1, 31)) + "\n"
    equal = "\n".join("10 10" for _ in range(30)) + "\n"
    white_heavy = "\n".join(f"{100-i} {i}" for i in range(30)) + "\n"
    black_heavy = "\n".join(f"{i} {100-i}" for i in range(30)) + "\n"
    mixed = "\n".join(f"{(i % 5) * 20} {((i + 2) % 5) * 20}" for i in range(32)) + "\n"
    cases = [
        edge(base),
        edge(equal),
        edge(white_heavy),
        edge(black_heavy),
        edge(mixed),
        stress("\n".join(f"{(i*7)%100} {(i*11)%100}" for i in range(35)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
