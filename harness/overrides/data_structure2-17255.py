from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    text = data.strip()
    seen: set[str] = set()

    def dfs(left: int, right: int, path: str) -> None:
        if left == 0 and right == len(text) - 1:
            seen.add(path)
            return
        if left > 0:
            dfs(left - 1, right, path + " " + text[left - 1:right + 1])
        if right + 1 < len(text):
            dfs(left, right + 1, path + " " + text[left:right + 2])

    for i in range(len(text)):
        dfs(i, i, text[i])
    return str(len(seen))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n"),
        edge("11\n"),
        edge("123\n"),
        edge("111\n"),
        edge("1234\n"),
        stress("1212\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
