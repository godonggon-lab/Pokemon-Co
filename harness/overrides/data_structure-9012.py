from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _is_vps(text: str) -> bool:
    count = 0
    for ch in text:
        count += 1 if ch == "(" else -1
        if count < 0:
            return False
    return count == 0


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    return "\n".join("YES" if _is_vps(text) else "NO" for text in lines[1:1 + n])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n()\n"),
        edge("1\n(\n"),
        edge("1\n)\n"),
        edge("3\n()\n(())\n(()\n"),
        edge("3\n())(()\n((()))\n()()()\n"),
        stress("5\n((((()))))\n()()()()\n(()())\n((())\n())(\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
