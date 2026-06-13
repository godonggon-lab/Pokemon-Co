from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 2\nNYY\nYNY\nYYN\n', '2 1 1\r\n'),
        edge('4 3\nNYYN\nYNYN\nYYNY\nNNYN\n', '2 1 2 1\r\n'),
        edge('2 1\nNY\nYN\n', '1 1\r\n'),
        edge('3 3\nNYY\nYNY\nYYN\n', '2 2 2\r\n'),
        edge('3 1\nNYY\nYNN\nYNN\n', '-1\r\n'),
        stress('5 4\nNYYNN\nYNYNN\nYYNYN\nNNYNY\nNNNYN\n', '2 1 2 2 1\r\n'),
    ]
