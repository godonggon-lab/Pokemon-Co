from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    it = iter(map(int, data.split()))
    t = next(it)
    queries = [(next(it), next(it)) for _ in range(t)]
    mod = 1_000_000_009
    mxn = max(n for n, _ in queries)
    mxm = max(m for _, m in queries)
    dp = [[0] * (mxm + 1) for _ in range(mxn + 1)]
    dp[0][0] = 1
    for total in range(1, mxn + 1):
        for cnt in range(1, mxm + 1):
            dp[total][cnt] = sum(
                dp[total - x][cnt - 1] for x in (1, 2, 3) if total >= x
            ) % mod
    out = []
    for n, m in queries:
        out.append(str(sum(dp[n][1 : m + 1]) % mod))
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 1\n"),
        edge("3\n3 3\n4 2\n5 5\n"),
        edge("3\n10 1\n10 5\n10 10\n"),
        edge("4\n2 1\n2 2\n3 1\n3 3\n"),
        edge("3\n6 2\n6 3\n6 6\n"),
        stress("3\n100 50\n200 100\n1000 500\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
