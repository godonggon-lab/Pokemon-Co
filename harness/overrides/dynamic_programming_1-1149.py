from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n26 40 83\n"),
        edge("3\n26 40 83\n49 60 57\n13 89 99\n"),
        edge("3\n1 100 100\n100 1 100\n100 100 1\n"),
        edge("4\n10 20 30\n30 20 10\n10 30 20\n20 10 30\n"),
        stress("20\n" + "\n".join(f"{(i*7)%100+1} {(i*11)%100+1} {(i*13)%100+1}" for i in range(20)) + "\n"),
    ]
