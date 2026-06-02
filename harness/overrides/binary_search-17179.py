from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    query_count, cut_count, length = map(int, lines[0].split())
    cuts = [int(line) for line in lines[1:1 + cut_count]] + [length]
    queries = [int(line) for line in lines[1 + cut_count:1 + cut_count + query_count]]

    def can(query: int, piece: int) -> bool:
        prev = count = 0
        for cut in cuts:
            if cut - prev >= piece:
                count += 1
                prev = cut
        return count >= query + 1

    out = []
    for query in queries:
        low, high = 1, length
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            if can(query, mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        out.append(str(answer))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1 10\n5\n1\n"), edge("2 3 20\n4\n10\n15\n1\n2\n"), stress("3 5 100\n10\n25\n40\n70\n90\n1\n2\n4\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
