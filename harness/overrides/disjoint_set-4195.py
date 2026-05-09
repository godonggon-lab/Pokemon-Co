from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    idx = 1
    out = []
    for _ in range(int(lines[0])):
        parent: dict[str, str] = {}
        size: dict[str, int] = {}

        def find(x: str) -> str:
            parent.setdefault(x, x)
            size.setdefault(x, 1)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for _ in range(int(lines[idx])):
            idx += 1
            a, b = lines[idx].split()
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
                size[ra] += size[rb]
            out.append(str(size[find(a)]))
        idx += 1
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n1\na b\n",
        "1\n2\na b\nb c\n",
        "1\n3\na b\nc d\na c\n",
        "2\n1\na b\n2\nx y\ny z\n",
        "1\n5\nFred Barney\nBarney Betty\nBetty Wilma\nDino Hoppy\nWilma Dino\n",
        "1\n6\na b\nc d\ne f\nb c\nd e\nf a\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
