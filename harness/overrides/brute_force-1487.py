from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n10 5\n"),
        edge("2\n10 11\n20 30\n"),
        edge("3\n10 1\n20 5\n30 10\n"),
        edge("4\n100 90\n80 10\n80 20\n50 1\n"),
        stress("10\n" + "\n".join(f"{(i+1)*10} {i*3}" for i in range(10)) + "\n"),
    ]
