from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\nabba\n', '0\r\n'),
        edge('1\nabca\n', '1\r\n'),
        edge('1\nabcda\n', '2\r\n'),
        edge('3\nabba\nabca\nabcda\n', '0\r\n1\r\n2\r\n'),
        edge('4\nsummuus\nxabba\nabbax\nabcddcba\n', '1\r\n1\r\n1\r\n0\r\n'),
        stress('5\nracecar\nabccbxa\nabcdef\nxyzyx\nabccaa\n', '0\r\n1\r\n2\r\n0\r\n2\r\n'),
    ]
