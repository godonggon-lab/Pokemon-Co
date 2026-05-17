from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    out: list[str] = []
    for token in stdin.split():
        if token == "0":
            break
        out.append("yes" if token == token[::-1] else "no")
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "0\n",
        "1\n0\n",
        "121\n1231\n12421\n0\n",
        "10\n11\n1001\n1234321\n123456\n0\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    values = ["9" * i for i in range(1, 20)] + ["123456789", "98765432123456789"]
    stdin = "\n".join(values + ["0"]) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
