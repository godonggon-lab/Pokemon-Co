from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    start, target = data.splitlines()
    possible = False

    def dfs(current: str) -> None:
        nonlocal possible
        if possible:
            return
        if len(current) == len(start):
            possible = current == start
            return
        if current.endswith("A"):
            dfs(current[:-1])
        if current.startswith("B"):
            dfs(current[1:][::-1])

    dfs(target)
    return "1" if possible else "0"

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("A\nBABA\n"),
        edge("AB\nABB\n"),
        edge("A\nABBA\n"),
        edge("B\nABBA\n"),
        edge("AB\nAB\n"),
        stress("AB\nABBABAABAB\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
