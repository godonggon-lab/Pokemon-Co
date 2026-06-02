from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    index = 1
    out = []
    for _ in range(int(lines[0])):
        target, n = map(int, lines[index].split())
        arrays = [list(map(int, lines[index + row].split())) for row in range(1, 5)]
        index += 5
        ab = sorted(a + b for a in arrays[0] for b in arrays[1])
        cd = sorted(c + d for c in arrays[2] for d in arrays[3])
        left, right = 0, len(cd) - 1
        best = ab[0] + cd[0]
        while left < len(ab) and right >= 0:
            total = ab[left] + cd[right]
            if abs(target - total) < abs(target - best) or (abs(target - total) == abs(target - best) and total < best):
                best = total
            if total < target:
                left += 1
            else:
                right -= 1
        out.append(str(best))
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n10 1\n1\n2\n3\n4\n"), edge("1\n25 3\n1 2 3\n4 5 6\n7 8 9\n10 11 12\n"), stress("1\n100 10\n" + "\n".join(" ".join(str((r*17+c*7)%50) for c in range(10)) for r in range(4)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
