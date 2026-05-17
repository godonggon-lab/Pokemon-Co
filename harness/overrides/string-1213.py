from __future__ import annotations

from collections import Counter
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    counter = Counter(s)
    odd = [ch for ch in sorted(counter) if counter[ch] % 2 == 1]
    if len(odd) > 1:
        return "I'm Sorry Hansoo"
    left = "".join(ch * (counter[ch] // 2) for ch in sorted(counter))
    middle = odd[0] if odd else ""
    return left + middle + left[::-1]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "AABB\n",
        "AAABB\n",
        "ABACABA\n",
        "ABC\n",
        "AAAA\n",
        "ZYXXYZ\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "A" * 20 + "B" * 18 + "C" * 12
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
