from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n10\n"),
        edge("2\n10\n20\n"),
        edge("3\n10\n20\n40\n"),
        edge("5\n1\n1\n1\n1\n1\n"),
        edge("6\n100\n1\n50\n2\n3\n4\n"),
        stress("30\n" + "\n".join(str((i * 17) % 100 + 1) for i in range(30)) + "\n"),
    ]
