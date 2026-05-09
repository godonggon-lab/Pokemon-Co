from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    parent: dict[int, int] = {}
    size: dict[int, int] = {}

    def find(x: int) -> int:
        parent.setdefault(x, x)
        size.setdefault(x, 1)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    out = []
    for line in lines[1:]:
        parts = line.split()
        if parts[0] == "I":
            a, b = map(int, parts[1:])
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
                size[ra] += size[rb]
        else:
            out.append(str(size[find(int(parts[1]))]))
    return "\n".join(out) + ("\n" if out else "")


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\nQ 1\n",
        "3\nI 1 2\nQ 1\nQ 3\n",
        "5\nI 1 2\nI 2 3\nQ 1\nI 4 5\nQ 5\n",
        "6\nI 10 20\nI 30 40\nQ 10\nI 20 30\nQ 40\nQ 50\n",
        "4\nI 1 1\nQ 1\nI 1 2\nQ 2\n",
        "8\nI 1 2\nI 3 4\nI 5 6\nQ 1\nI 2 3\nQ 4\nI 4 5\nQ 6\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
