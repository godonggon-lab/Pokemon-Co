from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    expression = data.strip()
    stack = []
    pairs = []
    for index, ch in enumerate(expression):
        if ch == "(":
            stack.append(index)
        elif ch == ")":
            pairs.append((stack.pop(), index))
    results = set()
    for mask in range(1, 1 << len(pairs)):
        removed = set()
        for i, pair in enumerate(pairs):
            if mask & (1 << i):
                removed.update(pair)
        results.add("".join(ch for i, ch in enumerate(expression) if i not in removed))
    return "\n".join(sorted(results))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("(a)\n"),
        edge("(a+b)\n"),
        edge("((a))\n"),
        edge("(a+(b))\n"),
        edge("((a+b)*(c+d))\n"),
        edge("((1+2)*(3+(4*5)))\n"),
        stress("(((a+b)*(c+d))+(e*(f+g)))\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
