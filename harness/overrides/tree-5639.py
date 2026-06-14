from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('5\n', '5\r\n'),
        edge('5\n3\n7\n', '3\r\n7\r\n5\r\n'),
        edge('1\n2\n3\n', '3\r\n2\r\n1\r\n'),
        edge('3\n2\n1\n', '1\r\n2\r\n3\r\n'),
        edge('2\n1\n3\n', '1\r\n3\r\n2\r\n'),
        stress('50\n30\n24\n5\n28\n45\n98\n52\n60\n', '5\r\n28\r\n24\r\n45\r\n30\r\n60\r\n52\r\n98\r\n50\r\n'),
    ]
