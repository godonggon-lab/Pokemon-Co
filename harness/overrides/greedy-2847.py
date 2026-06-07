from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n10\n', '0\r\n'),
        edge('3\n1\n2\n3\n', '0\r\n'),
        edge('3\n5\n5\n5\n', '3\r\n'),
        edge('4\n10\n9\n8\n7\n', '12\r\n'),
        edge('5\n10\n20\n20\n30\n30\n', '2\r\n'),
        stress('20\n100\n100\n99\n99\n98\n98\n97\n97\n96\n96\n95\n95\n94\n94\n93\n93\n92\n92\n91\n91\n', '280\r\n'),
    ]
