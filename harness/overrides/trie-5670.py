from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\nhello\nhell\nheaven\n', '2.33\r\n'),
        edge('2\na\nb\n', '1.00\r\n'),
        stress('5\ngo\ngone\nguild\ngold\ngoal\n', '2.60\r\n'),
    ]
