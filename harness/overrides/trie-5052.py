from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n3\n911\n97625999\n91125426\n', 'NO\r\n'),
        edge('1\n3\n113\n12340\n123440\n', 'YES\r\n'),
        edge('2\n2\n1\n12\n3\n12\n34\n56\n', 'NO\r\nYES\r\n'),
        stress('1\n10\n100000\n100037\n100074\n100111\n100148\n100185\n100222\n100259\n100296\n100333\n', 'YES\r\n'),
    ]
