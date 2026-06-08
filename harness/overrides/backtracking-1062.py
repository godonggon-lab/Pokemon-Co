from __future__ import annotations
import itertools
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, k = map(int, lines[0].split())
    base = set("antic")
    masks = []
    for word in lines[1 : 1 + n]:
        mask = 0
        for ch in set(word) - base:
            mask |= 1 << (ord(ch) - 97)
        masks.append(mask)
    if k < 5:
        return "0"
    if k == 26:
        return str(n)
    candidates = [i for i in range(26) if chr(i + 97) not in base]
    answer = 0
    for comb in itertools.combinations(candidates, k - 5):
        taught = 0
        for bit in comb:
            taught |= 1 << bit
        answer = max(answer, sum((mask & ~taught) == 0 for mask in masks))
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 4\nantatica\n"),
        edge("1 5\nantatica\n"),
        edge("2 26\nantabtica\nantaztica\n"),
        edge("4 5\nantatica\nantabtica\nantactica\nantadtica\n"),
        edge("3 6\nantarctica\nantahellotica\nantacartica\n"),
        stress("5 7\nantabtica\nantaztica\nantaytica\nantabytica\nantaxyztica\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
