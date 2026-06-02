from __future__ import annotations
import bisect
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    gun_count, animal_count, limit = map(int, lines[0].split())
    guns = sorted(map(int, lines[1].split()))
    answer = 0
    for line in lines[2:2 + animal_count]:
        x, y = map(int, line.split())
        index = bisect.bisect_left(guns, x)
        ok = False
        for candidate in (index - 1, index):
            if 0 <= candidate < gun_count and abs(guns[candidate] - x) + y <= limit:
                ok = True
        answer += ok
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1 1\n0\n0 1\n"), edge("4 8 4\n6 1 4 9\n7 2\n3 3\n4 5\n5 1\n2 2\n1 4\n8 4\n9 4\n"), stress("20 20 30\n" + " ".join(str(i*10) for i in range(20)) + "\n" + "\n".join(f"{i*7} {i%10}" for i in range(20)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
