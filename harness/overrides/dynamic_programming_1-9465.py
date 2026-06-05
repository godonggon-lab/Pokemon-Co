from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    t = nums[0]
    idx = 1
    out = []
    for _ in range(t):
        n = nums[idx]
        idx += 1
        top = nums[idx : idx + n]
        idx += n
        bottom = nums[idx : idx + n]
        idx += n
        if n == 1:
            out.append(str(max(top[0], bottom[0])))
            continue
        dp_top = [0] * n
        dp_bottom = [0] * n
        dp_top[0], dp_bottom[0] = top[0], bottom[0]
        dp_top[1] = bottom[0] + top[1]
        dp_bottom[1] = top[0] + bottom[1]
        for i in range(2, n):
            dp_top[i] = max(dp_bottom[i - 1], dp_bottom[i - 2]) + top[i]
            dp_bottom[i] = max(dp_top[i - 1], dp_top[i - 2]) + bottom[i]
        out.append(str(max(dp_top[-1], dp_bottom[-1])))
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1\n50\n30\n"),
        edge("1\n2\n10 20\n30 40\n"),
        edge("1\n5\n50 10 100 20 40\n30 50 70 10 60\n"),
        edge("2\n1\n1\n100\n3\n10 30 10\n20 10 40\n"),
        edge("1\n4\n1 100 1 100\n100 1 100 1\n"),
        stress("1\n10\n" + " ".join(str((i * 7) % 101) for i in range(10)) + "\n" + " ".join(str((i * 11) % 101) for i in range(10)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
