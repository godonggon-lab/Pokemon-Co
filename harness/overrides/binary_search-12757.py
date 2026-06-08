from __future__ import annotations

import bisect
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m, limit = map(int, lines[0].split())
    keys = []
    values = {}
    for line in lines[1:1 + n]:
        key, value = map(int, line.split())
        keys.append(key)
        values[key] = value
    keys.sort()
    out = []

    def nearest(key: int) -> int | str | None:
        index = bisect.bisect_left(keys, key)
        candidates = []
        if index < len(keys):
            candidates.append(keys[index])
        if index:
            candidates.append(keys[index - 1])
        candidates = [candidate for candidate in candidates if abs(candidate - key) <= limit]
        if not candidates:
            return None
        candidates.sort(key=lambda item: (abs(item - key), item))
        if len(candidates) >= 2 and abs(candidates[0] - key) == abs(candidates[1] - key):
            return "?"
        return candidates[0]

    for line in lines[1 + n:1 + n + m]:
        query = list(map(int, line.split()))
        if query[0] == 1:
            _, key, value = query
            if key not in values:
                bisect.insort(keys, key)
            values[key] = value
        elif query[0] == 2:
            _, key, value = query
            target = nearest(key)
            if isinstance(target, int):
                values[target] = value
        else:
            _, key = query
            target = nearest(key)
            if target is None:
                out.append("-1")
            elif target == "?":
                out.append("?")
            else:
                out.append(str(values[target]))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 3 1\n10 100\n20 200\n3 10\n3 11\n3 15\n"),
        edge("1 3 0\n5 50\n3 5\n2 5 55\n3 5\n"),
        edge("2 4 3\n10 100\n20 200\n3 15\n2 12 120\n3 10\n3 12\n"),
        edge("2 3 5\n10 100\n20 200\n3 15\n1 15 150\n3 15\n"),
        edge("2 4 2\n10 100\n14 140\n3 12\n2 12 120\n1 12 999\n3 12\n"),
        stress("3 6 2\n5 50\n10 100\n20 200\n3 7\n1 8 80\n3 9\n2 19 190\n3 20\n3 14\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
