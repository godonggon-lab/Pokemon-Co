from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('00:00:00\n00:00:00\n', '24:00:00\r\n'),
        edge('00:00:00\n00:00:01\n', '00:00:01\r\n'),
        edge('23:59:59\n00:00:00\n', '00:00:01\r\n'),
        edge('12:34:56\n12:35:56\n', '00:01:00\r\n'),
        edge('10:00:00\n09:00:00\n', '23:00:00\r\n'),
        stress('01:02:03\n04:05:06\n', '03:03:03\r\n'),
    ]
