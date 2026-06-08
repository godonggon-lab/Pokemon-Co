from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 3 1 3\n1\n2\n', '2\r\n'),
        edge('8 30 4 30\n7\n9\n7\n30\n2\n7\n9\n25\n', '5\r\n'),
        edge('5 5 3 4\n1\n2\n3\n2\n1\n', '4\r\n'),
        stress('30 10 5 7\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n', '6\r\n'),
    ]
