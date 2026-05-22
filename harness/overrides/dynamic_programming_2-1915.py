from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n"),
        edge("1 1\n1\n"),
        edge("4 4\n1111\n1111\n1111\n1111\n"),
        edge("4 5\n10100\n10111\n11111\n10010\n"),
        stress("20 20\n" + "\n".join(("10" * 10) if i % 2 else ("01" * 10) for i in range(20)) + "\n"),
    ]
