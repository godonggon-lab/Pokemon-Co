from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    gates = int(lines[0])
    planes = int(lines[1])
    parent = list(range(gates + 1))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    answer = 0
    for line in lines[2:2 + planes]:
        gate = find(int(line))
        if gate == 0:
            break
        parent[gate] = find(gate - 1)
        answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1\n1\n"),
        edge("2\n2\n1\n1\n"),
        edge("4\n3\n4\n1\n1\n"),
        edge("4\n6\n2\n2\n3\n3\n4\n4\n"),
        edge("5\n5\n5\n4\n3\n2\n1\n"),
        stress("10\n12\n10\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
