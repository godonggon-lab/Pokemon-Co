from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2\n1 1\n', '1\r\n'),
        edge('2\n6 10\n', '1\r\n2\r\n'),
        edge('3\n12 18 24\n', '1\r\n2\r\n3\r\n6\r\n'),
        edge('3\n7 11 13\n', '1\r\n'),
        edge('2\n100 250\n', '1\r\n2\r\n5\r\n10\r\n25\r\n50\r\n'),
        stress('3\n360 720 1080\n', '1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n8\r\n9\r\n10\r\n12\r\n15\r\n18\r\n20\r\n24\r\n30\r\n36\r\n40\r\n45\r\n60\r\n72\r\n90\r\n120\r\n180\r\n360\r\n'),
    ]
