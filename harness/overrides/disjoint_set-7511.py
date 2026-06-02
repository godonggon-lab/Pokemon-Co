from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    t = int(lines[0])
    cursor = 1
    out = []
    for case in range(1, t + 1):
        n = int(lines[cursor])
        cursor += 1
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        m = int(lines[cursor])
        cursor += 1
        for line in lines[cursor:cursor + m]:
            a, b = map(int, line.split())
            union(a, b)
        cursor += m
        q = int(lines[cursor])
        cursor += 1
        out.append(f"Scenario {case}:")
        for line in lines[cursor:cursor + q]:
            a, b = map(int, line.split())
            out.append("1" if find(a) == find(b) else "0")
        cursor += q
        out.append("")
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n3\n1\n0 1\n2\n0 1\n1 2\n"), stress("2\n4\n2\n0 1\n2 3\n3\n0 1\n1 2\n2 3\n3\n0\n2\n0 1\n1 2\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
