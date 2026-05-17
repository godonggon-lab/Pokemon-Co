from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    _, path = stdin.split()
    return str(sum(1 for i in range(len(path) - 1) if path[i:i + 2] == "EW"))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2\nEW\n",
        "5\nEEEWW\n",
        "6\nEWEWEW\n",
        "7\nWWEEEWW\n",
        "10\nEEEEWWWWWW\n",
        "12\nEWWEEWWEWWEW\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    path = "E" * 500 + "W" * 500
    cases.append(stress(f"{len(path)}\n{path}\n", _solve(f"{len(path)}\n{path}\n")))
    return cases
