from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


TOP = "www\nwww\nwww\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\nU+\n", TOP),
        edge("1\n1\nU-\n", TOP),
        edge("1\n2\nU+ U-\n", TOP),
        edge("1\n2\nF+ F-\n", TOP),
        edge("1\n2\nL+ L-\n", TOP),
        stress("2\n1\nU+\n2\nR+ R-\n", TOP + TOP),
    ]
