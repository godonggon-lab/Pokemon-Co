from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 1\nS0K\n000\n000\n', '2\r\n'),
        edge('3 1\nS1K\n111\n000\n', '-1\r\n'),
        edge('2 0\nS0\n00\n', '0\r\n'),
        edge('3 2\nSK0\n000\n00K\n', '4\r\n'),
        edge('4 2\nS000\n1110\nK000\n000K\n', '10\r\n'),
        stress('5 2\nS0000\n01110\n0K0K0\n01110\n00000\n', '5\r\n'),
    ]
