from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    dp = [[0] * 31 for _ in range(31)]

    def solve(whole: int, half: int) -> int:
        if whole == 0:
            return 1
        if dp[whole][half]:
            return dp[whole][half]
        answer = solve(whole - 1, half + 1)
        if half:
            answer += solve(whole, half - 1)
        dp[whole][half] = answer
        return answer

    out = []
    for value in map(int, data.split()):
        if value == 0:
            break
        out.append(str(solve(value, 0)))
    return "\n".join(out) + ("\n" if out else "")


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("1\n0\n"), edge("1\n2\n3\n0\n"), stress("30\n29\n28\n0\n")])
