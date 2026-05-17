from __future__ import annotations

from collections import Counter
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    t = int(lines[0])
    out: list[str] = []
    for line in lines[1 : 1 + t]:
        a, b = line.split()
        verdict = "are anagrams." if Counter(a) == Counter(b) else "are NOT anagrams."
        out.append(f"{a} & {b} {verdict}")
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3\nblather reblath\nmaryland landam\nbizarre brazier\n",
        "2\na a\nab ba\n",
        "3\nabc abd\naabb bbaa\nAa aA\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    pairs = [(f"word{i}", "".join(sorted(f"word{i}"))) for i in range(50)]
    stdin = f"{len(pairs)}\n" + "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
