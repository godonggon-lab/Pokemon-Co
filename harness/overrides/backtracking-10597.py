from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    n = len(s) if len(s) <= 9 else 9 + (len(s) - 9) // 2
    used = [False] * (n + 1)
    answer: list[int] = []

    def dfs(idx: int) -> bool:
        if idx == len(s):
            return len(answer) == n
        for width in (1, 2):
            part = s[idx : idx + width]
            if not part:
                continue
            value = int(part)
            if 1 <= value <= n and not used[value]:
                used[value] = True
                answer.append(value)
                if dfs(idx + width):
                    return True
                answer.pop()
                used[value] = False
        return False

    dfs(0)
    return " ".join(map(str, answer))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("123456789\n"),
        edge("987654321\n"),
        edge("12345678910\n"),
        edge("123456789101112\n"),
        edge("1234567891011\n"),
        edge("1211109876543\n"),
        stress("10987654321\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
