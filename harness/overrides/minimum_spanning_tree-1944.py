from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 1\nS0K\n000\n000\n', '2\r\n'),
        edge('3 1\nS1K\n111\n000\n', '-1\r\n'),
        stress('5 2\nS0000\n01110\n0K0K0\n01110\n00000\n', '5\r\n'),
    ]
