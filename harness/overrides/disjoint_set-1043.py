from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    truth = set(map(int, lines[1].split()[1:]))
    parties = [list(map(int, line.split()))[1:] for line in lines[2:]]
    changed = True
    while changed:
        changed = False
        for party in parties:
            if truth.intersection(party):
                before = len(truth)
                truth.update(party)
                changed |= len(truth) != before
    return f"{sum(1 for party in parties if not truth.intersection(party))}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1 1\n0\n1 1\n",
        "3 2\n1 1\n2 1 2\n1 3\n",
        "4 3\n1 1\n2 1 2\n2 2 3\n1 4\n",
        "4 3\n0\n2 1 2\n2 2 3\n1 4\n",
        "5 4\n2 1 5\n2 1 2\n2 2 3\n2 3 4\n2 4 5\n",
        "6 5\n1 6\n2 1 2\n2 2 3\n1 4\n2 4 5\n2 5 6\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
