from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    text = data.strip()
    stack = []
    current = 1
    answer = 0
    previous = ""
    for ch in text:
        if ch == "(":
            stack.append(ch)
            current *= 2
        elif ch == "[":
            stack.append(ch)
            current *= 3
        elif ch == ")":
            if not stack or stack[-1] != "(":
                return "0"
            if previous == "(":
                answer += current
            stack.pop()
            current //= 2
        elif ch == "]":
            if not stack or stack[-1] != "[":
                return "0"
            if previous == "[":
                answer += current
            stack.pop()
            current //= 3
        previous = ch
    return str(answer if not stack else 0)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("()\n"),
        edge("[]\n"),
        edge("([])\n"),
        edge("()[[]]\n"),
        edge("([)]\n"),
        stress("(()[[]])([])\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
