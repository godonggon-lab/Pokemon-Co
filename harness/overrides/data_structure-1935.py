from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    expression = lines[1]
    values = {chr(ord("A") + i): float(lines[2 + i]) for i in range(n)}
    stack = []
    for token in expression:
        if token.isalpha():
            stack.append(values[token])
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
    return f"{stack[-1]:.2f}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\nA\n5\n"),
        edge("2\nAB+\n1\n2\n"),
        edge("2\nAB-\n1\n2\n"),
        edge("2\nAB/\n5\n2\n"),
        edge("3\nAB*C+\n2\n3\n4\n"),
        stress("5\nABC*+DE/-\n1\n2\n3\n4\n5\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
