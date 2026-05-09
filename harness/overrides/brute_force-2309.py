from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("20\n7\n23\n19\n10\n15\n25\n8\n13\n"),
        edge("1\n2\n3\n4\n5\n6\n79\n8\n9\n"),
        edge("10\n11\n12\n13\n14\n15\n25\n1\n2\n"),
        edge("30\n25\n20\n10\n5\n4\n6\n40\n60\n"),
        edge("6\n7\n8\n9\n10\n20\n40\n1\n99\n"),
        edge("50\n1\n2\n3\n4\n5\n35\n10\n90\n"),
    ]
