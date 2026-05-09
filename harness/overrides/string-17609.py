from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nabba\n"),
        edge("1\nabca\n"),
        edge("1\nabcda\n"),
        edge("3\nabba\nabca\nabcda\n"),
        edge("4\nsummuus\nxabba\nabbax\nabcddcba\n"),
        stress("5\nracecar\nabccbxa\nabcdef\nxyzyx\nabccaa\n"),
    ]
