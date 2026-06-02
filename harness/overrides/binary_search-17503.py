from __future__ import annotations
import heapq
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    need_count, need_favor, beer_count = map(int, lines[0].split())
    beers = sorted((tuple(map(int, line.split())) for line in lines[1:1 + beer_count]), key=lambda item: item[1])
    heap = []
    favor_sum = 0
    for favor, level in beers:
        heapq.heappush(heap, favor)
        favor_sum += favor
        if len(heap) > need_count:
            favor_sum -= heapq.heappop(heap)
        if len(heap) == need_count and favor_sum >= need_favor:
            return str(level)
    return "-1"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 10 1\n10 5\n"), edge("2 10 3\n3 1\n7 2\n4 3\n"), stress("3 20 5\n5 3\n8 4\n10 5\n2 1\n9 6\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
