from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _valid(candidate: str) -> bool:
    return "0" not in candidate and len(set(candidate)) == 3


def _score(candidate: str, guess: str) -> tuple[int, int]:
    strike = sum(candidate[i] == guess[i] for i in range(3))
    ball = 0
    for i in range(3):
        for j in range(3):
            if i != j and candidate[i] == guess[j]:
                ball += 1
    return strike, ball


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    hints = []
    for line in lines[1:1 + n]:
        guess, strike, ball = line.split()
        hints.append((guess, int(strike), int(ball)))
    answer = 0
    for value in range(123, 988):
        candidate = str(value)
        if _valid(candidate) and all(_score(candidate, guess) == (strike, ball) for guess, strike, ball in hints):
            answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n123 3 0\n"),
        edge("1\n123 0 0\n"),
        edge("2\n123 1 1\n356 1 0\n"),
        edge("3\n123 1 1\n456 0 0\n178 1 0\n"),
        edge("4\n123 1 1\n124 2 0\n125 2 0\n126 2 0\n"),
        stress("5\n123 1 1\n356 1 0\n327 2 0\n489 0 1\n789 0 0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
