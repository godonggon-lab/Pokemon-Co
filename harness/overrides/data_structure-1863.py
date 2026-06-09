from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    stack = [0]
    answer = 0
    for line in lines[1:1 + n]:
        _x, height = map(int, line.split())
        while stack[-1] > height:
            stack.pop()
            answer += 1
        if stack[-1] < height:
            stack.append(height)
    answer += len(stack) - 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 0\n"),
        edge("3\n1 1\n2 1\n3 1\n"),
        edge("4\n1 1\n2 2\n3 1\n4 0\n"),
        edge("5\n1 3\n2 3\n3 2\n4 2\n5 0\n"),
        edge("6\n1 1\n2 2\n3 3\n4 2\n5 1\n6 0\n"),
        stress("20\n" + "\n".join(f"{i} {(i * 7) % 5}" for i in range(1, 21)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
