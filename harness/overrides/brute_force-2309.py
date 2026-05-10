from __future__ import annotations

from itertools import combinations
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    heights = list(map(int, stdin.split()))
    for picked in combinations(heights, 7):
        if sum(picked) == 100:
            return "\n".join(map(str, sorted(picked))) + "\n"
    return ""


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "20\n7\n23\n19\n10\n15\n25\n8\n13\n",
        "1\n2\n3\n4\n5\n6\n79\n8\n9\n",
        "10\n11\n12\n13\n14\n15\n25\n1\n2\n",
        "30\n25\n20\n10\n5\n4\n6\n40\n60\n",
        "6\n7\n8\n9\n10\n20\n40\n1\n99\n",
        "50\n1\n2\n3\n4\n5\n35\n10\n90\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "11\n12\n13\n14\n15\n16\n19\n21\n80\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
