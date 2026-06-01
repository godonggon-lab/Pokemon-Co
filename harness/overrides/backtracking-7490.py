from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    out = []
    for case_index in range(int(lines[0])):
        n = int(lines[case_index + 1])
        rows = []

        def dfs(value: int, expr: str) -> None:
            if value == n:
                if eval(expr.replace(" ", "")) == 0:
                    rows.append(expr)
                return
            for op in (" ", "+", "-"):
                dfs(value + 1, expr + op + str(value + 1))

        dfs(1, "1")
        out.extend(rows)
        out.append("")
    return "\n".join(out).rstrip()


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n3\n"), stress("2\n3\n7\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
