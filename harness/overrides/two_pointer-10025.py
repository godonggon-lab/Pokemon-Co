from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 0\n5 10\n', '5\r\n'),
        edge('4 1\n1 0\n2 1\n3 2\n4 10\n', '6\r\n'),
        stress('30 10\n1 0\n2 100\n3 200\n4 300\n5 400\n6 500\n7 600\n8 700\n9 800\n1 900\n2 1000\n3 1100\n4 1200\n5 1300\n6 1400\n7 1500\n8 1600\n9 1700\n1 1800\n2 1900\n3 2000\n4 2100\n5 2200\n6 2300\n7 2400\n8 2500\n9 2600\n1 2700\n2 2800\n3 2900\n', '9\r\n'),
    ]
