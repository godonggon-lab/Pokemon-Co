from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("2\n"), edge("7\n"), stress("99\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]

def _solve(data: str) -> str:
    n = int(data)
    lines = []
    for bit in range(7):
        chars = []
        for i in range(n):
            chars.append("A" if (i >> bit) & 1 else "B")
        lines.append("".join(chars))
    return "\n".join(lines)

def check_output(stdin: str, _expected: str, actual: str) -> bool:
    n = int(stdin.strip())
    lines = [line.strip() for line in actual.strip().splitlines() if line.strip()]
    if len(lines) != 7:
        return False
    if any(len(line) != n or any(ch not in "AB" for ch in line) for line in lines):
        return False
    for i in range(n):
        for j in range(i + 1, n):
            if all(line[i] == line[j] for line in lines):
                return False
    return True
