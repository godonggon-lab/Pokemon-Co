from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    if "::" in s:
        left, right = s.split("::")
        left_parts = left.split(":") if left else []
        right_parts = right.split(":") if right else []
        parts = left_parts + ["0"] * (8 - len(left_parts) - len(right_parts)) + right_parts
    else:
        parts = s.split(":")
    return ":".join(part.zfill(4) for part in parts)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "25:09:1985:aa:091:4846:374:bb\n",
        "::1\n",
        "2001:db8::ff00:42:8329\n",
        "::\n",
        "1:2:3:4:5:6:7:8\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    hard = "2001:0db8:0000:0000:0000:ff00:0042:8329\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
