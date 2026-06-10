from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    text = lines[0].strip()
    n = int(lines[1])
    bonus = []
    for line in lines[2:2 + n]:
        pattern, score = line.split()
        bonus.append((pattern, int(score)))
    dp = [0] * (len(text) + 1)
    for i in range(len(text)):
        dp[i + 1] = max(dp[i + 1], dp[i] + 1)
        for pattern, score in bonus:
            if text.startswith(pattern, i):
                dp[i + len(pattern)] = max(dp[i + len(pattern)], dp[i] + score)
    return f"{dp[-1]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("abc\n1\nab 5\n"),
        edge("aaaa\n2\na 3\naa 10\n"),
        edge("a\n0\n"),
        edge("abcabc\n2\nabc 10\nbc 4\n"),
        edge("aaaaa\n2\naa 3\naaa 10\n"),
        stress("banana\n3\nba 5\nna 4\nbanana 20\n"),
    ])
