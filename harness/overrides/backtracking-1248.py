from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    raw = lines[1].strip()
    signs = [[""] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(i, n):
            signs[i][j] = raw[idx]
            idx += 1
    answer: list[int] = []

    def ok(pos: int) -> bool:
        total = 0
        for i in range(pos, -1, -1):
            total += answer[i]
            if signs[i][pos] == "+" and total <= 0:
                return False
            if signs[i][pos] == "-" and total >= 0:
                return False
            if signs[i][pos] == "0" and total != 0:
                return False
        return True

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        candidates = [0] if signs[pos][pos] == "0" else (range(1, 11) if signs[pos][pos] == "+" else range(-10, 0))
        for value in candidates:
            answer.append(value)
            if ok(pos) and dfs(pos + 1):
                return True
            answer.pop()
        return False

    dfs(0)
    return " ".join(map(str, answer))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n+\n"), edge("2\n-++\n"), stress("4\n-00++++0++\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
