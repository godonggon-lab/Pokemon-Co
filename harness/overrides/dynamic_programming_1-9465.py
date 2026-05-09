from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n50\n30\n"),
        edge("1\n2\n10 20\n30 40\n"),
        edge("1\n5\n50 10 100 20 40\n30 50 70 10 60\n"),
        edge("2\n1\n1\n100\n3\n10 30 10\n20 10 40\n"),
        edge("1\n4\n1 100 1 100\n100 1 100 1\n"),
        stress("1\n10\n" + " ".join(str((i * 7) % 101) for i in range(10)) + "\n" + " ".join(str((i * 11) % 101) for i in range(10)) + "\n"),
    ]
