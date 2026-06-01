from __future__ import annotations
from collections import Counter
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    out = []
    for word in lines[1:1 + int(lines[0])]:
        counter = Counter(word)
        chars = sorted(counter)
        current = []

        def dfs() -> None:
            if len(current) == len(word):
                out.append("".join(current))
                return
            for char in chars:
                if counter[char]:
                    counter[char] -= 1
                    current.append(char)
                    dfs()
                    current.pop()
                    counter[char] += 1

        dfs()
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\nab\n"), edge("1\naab\n"), stress("2\nabc\naabb\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
