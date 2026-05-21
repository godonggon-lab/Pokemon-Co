from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge

PATTERNS = [
    ["***", "* *", "* *", "* *", "***"],
    ["  *", "  *", "  *", "  *", "  *"],
    ["***", "  *", "***", "*  ", "***"],
    ["***", "  *", "***", "  *", "***"],
    ["* *", "* *", "***", "  *", "  *"],
    ["***", "*  ", "***", "  *", "***"],
    ["***", "*  ", "***", "* *", "***"],
    ["***", "  *", "  *", "  *", "  *"],
    ["***", "* *", "***", "* *", "***"],
    ["***", "* *", "***", "  *", "***"],
]


def _render(value: str) -> str:
    rows = []
    for r in range(5):
        rows.append(" ".join(PATTERNS[int(ch)][r] for ch in value))
    return "\n".join(rows) + "\n"


def _solve(stdin: str) -> str:
    rows = stdin.splitlines()
    try:
        count = (len(rows[0]) + 1) // 4
        digits = []
        for idx in range(count):
            block = [row[idx * 4 : idx * 4 + 3] for row in rows[:5]]
            digits.append(PATTERNS.index(block))
        value = int("".join(map(str, digits)))
        return "BEER!!" if value % 6 == 0 else "BOOM!!"
    except Exception:
        return "BOOM!!"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    valid = [_render("12"), _render("18"), _render("100002")]
    invalid = _render("12").replace("*", " ", 1)
    return [edge(stdin, _solve(stdin)) for stdin in [*valid, invalid]]
