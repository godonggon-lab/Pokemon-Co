from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n10\n"),
        edge("2\n10\n20\n"),
        edge("3\n10\n20\n15\n"),
        edge("4\n10\n20\n15\n25\n"),
        edge("6\n10\n20\n15\n25\n10\n20\n"),
        stress("10\n" + "\n".join(str((i * 7) % 30 + 1) for i in range(10)) + "\n"),
    ]
