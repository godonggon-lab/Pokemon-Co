from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _shuffle(card1: list[int], card2: list[int], card3: list[int]) -> list[int]:
    if len(card2) > 1:
        half = len(card2) // 2
        return _shuffle(card2[:half] + card1, card2[half:], card3)
    return card2 + card1 + card3


def _apply(cards: list[int], k: int) -> list[int]:
    size = 2**k
    return _shuffle([], cards[len(cards) - size:], cards[:len(cards) - size])


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    target = list(map(int, lines[1].split()))
    orders = list(range(1, 10))
    for first in orders:
        for second in orders:
            if 2 ** max(first, second) >= n:
                continue
            cards = list(range(1, n + 1))
            cards = _apply(cards, first)
            cards = _apply(cards, second)
            if cards == target:
                return f"{first} {second}"
    return ""


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("4\n2 1 4 3\n"),
        edge("5\n3 2 5 4 1\n"),
        edge("5\n3 2 4 1 5\n"),
        edge("8\n6 5 8 7 1 2 3 4\n"),
        edge("8\n4 3 1 2 8 7 5 6\n"),
        stress("10\n8 7 5 6 1 2 3 4 10 9\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
