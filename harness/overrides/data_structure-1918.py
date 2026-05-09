from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("A+B\n", "AB+\n"),
        edge("A+B*C\n", "ABC*+\n"),
        edge("(A+B)*C\n", "AB+C*\n"),
        edge("A*(B+C)\n", "ABC+*\n"),
        edge("A+B*C-D/E\n", "ABC*+DE/-\n"),
        stress("((A+B)*C-(D-E))*(F+G)\n", "AB+C*DE--FG+*\n"),
    ]
