from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    i = 0
    while i < len(s):
        count = 0
        while i < len(s) and s[i] == "w":
            count += 1
            i += 1
        if count == 0:
            return "0"
        for ch in "olf":
            current = 0
            while i < len(s) and s[i] == ch:
                current += 1
                i += 1
            if current != count:
                return "0"
    return "1" if i == len(s) else "0"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "wolf\n",
        "wwoollff\n",
        "wolfwwoollff\n",
        "woolf\n",
        "wwolff\n",
        "olf\n",
        "wolfwolfw\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "".join("w" * i + "o" * i + "l" * i + "f" * i for i in range(1, 30))
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
