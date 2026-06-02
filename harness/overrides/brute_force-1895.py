from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    r, c = map(int, lines[0].split())
    arr = [list(map(int, line.split())) for line in lines[1:1 + r]]
    threshold = int(lines[1 + r])
    answer = 0
    for i in range(r - 2):
        for j in range(c - 2):
            values = []
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    values.append(arr[x][y])
            values.sort()
            if values[4] >= threshold:
                answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3 3\n1 2 3\n4 5 6\n7 8 9\n5\n"),
        edge("4 4\n1 1 1 1\n1 9 9 1\n1 9 9 1\n1 1 1 1\n5\n"),
        edge("3 4\n10 20 30 40\n50 60 70 80\n90 100 110 120\n60\n"),
        stress("10 10\n" + "\n".join(" ".join(str((r * 13 + c * 7) % 256) for c in range(10)) for r in range(10)) + "\n100\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
