from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, pack_goal = map(int, lines[0].split())
    cards = list(map(int, lines[1].split()))

    def ok(length: int) -> bool:
        used = set()
        packs = count = left = 0
        for right, card in enumerate(cards):
            while card in used:
                used.remove(cards[left])
                left += 1
                count -= 1
            used.add(card)
            count += 1
            if count == length:
                packs += 1
                used.clear()
                count = 0
                left = right + 1
        return packs >= pack_goal

    low, high = 0, n
    while low < high:
        mid = (low + high + 1) // 2
        if ok(mid):
            low = mid
        else:
            high = mid - 1
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("3 1\n1 2 3\n"), edge("5 2\n1 2 1 3 4\n"), stress("10 3\n1 2 3 1 2 4 5 6 4 7\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
