from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    t = nums[0]
    idx = 1
    out = []
    for _ in range(t):
        k = nums[idx]
        idx += 1
        a = [0] + nums[idx : idx + k]
        idx += k
        prefix = [0] * (k + 1)
        for i in range(1, k + 1):
            prefix[i] = prefix[i - 1] + a[i]
        dp = [[0] * (k + 1) for _ in range(k + 1)]
        for length in range(2, k + 1):
            for left in range(1, k - length + 2):
                right = left + length - 1
                dp[left][right] = min(dp[left][mid] + dp[mid + 1][right] for mid in range(left, right)) + prefix[right] - prefix[left - 1]
        out.append(str(dp[1][k]))
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n1\n7\n"), edge("1\n4\n40 30 30 50\n"), stress("2\n5\n1 2 3 4 5\n6\n10 20 30 40 50 60\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
