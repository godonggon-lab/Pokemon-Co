from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    k = int(lines[0])
    ops = lines[1].split()
    answers = []
    used = [False] * 10

    def good(a: int, op: str, b: int) -> bool:
        return a < b if op == "<" else a > b

    def dfs(path: list[int]) -> None:
        if len(path) == k + 1:
            answers.append("".join(map(str, path)))
            return
        for digit in range(10):
            if not used[digit] and (not path or good(path[-1], ops[len(path) - 1], digit)):
                used[digit] = True
                path.append(digit)
                dfs(path)
                path.pop()
                used[digit] = False

    dfs([])
    return f"{max(answers)}\n{min(answers)}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n<\n"), edge("2\n< >\n"), stress("4\n< > < >\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
