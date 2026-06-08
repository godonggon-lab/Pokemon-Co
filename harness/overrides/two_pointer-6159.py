from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 10\n4\n6\n', '1\r\n'),
        edge('4 10\n1\n2\n8\n9\n', '4\r\n'),
        edge('5 5\n5\n5\n5\n1\n1\n', '1\r\n'),
        stress('30 50\n1\n8\n15\n22\n29\n36\n43\n50\n57\n4\n11\n18\n25\n32\n39\n46\n53\n60\n7\n14\n21\n28\n35\n42\n49\n56\n3\n10\n17\n24\n', '178\r\n'),
    ]
