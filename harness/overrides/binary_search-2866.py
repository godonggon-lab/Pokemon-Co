from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    rows_count, cols_count = map(int, lines[0].split())
    rows = lines[1:1 + rows_count]
    cols = ["".join(rows[row][col] for row in range(rows_count)) for col in range(cols_count)]
    answer = 0
    for cut in range(rows_count):
        seen = set()
        ok = True
        for col in cols:
            tail = col[cut:]
            if tail in seen:
                ok = False
                break
            seen.add(tail)
        if ok:
            answer = cut
        else:
            break
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 2\nab\ncd\n"),
        edge("3 2\naa\nbb\naa\n"),
        edge("3 3\nabc\nabc\nabc\n"),
        edge("4 2\nab\ncd\nef\ngh\n"),
        edge("5 4\nabcd\nefgh\nijkl\nmnop\nqrst\n"),
        stress("4 3\nabc\ndef\nghi\njkl\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
