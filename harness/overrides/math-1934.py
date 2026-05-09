from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 1\n", "1\n"),
        edge("1\n2 3\n", "6\n"),
        edge("2\n6 8\n12 18\n", "24\n36\n"),
        edge("3\n1 999\n13 17\n100 25\n", "999\n221\n100\n"),
        edge("4\n10 20\n21 6\n14 15\n9 28\n", "20\n42\n210\n252\n"),
        stress("5\n100 75\n81 27\n17 34\n22 33\n999 37\n", "300\n81\n34\n66\n999\n"),
    ]
