from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\nN\n', '0\r\n'),
        edge('2\nNY\nYN\n', '1\r\n'),
        edge('3\nNYN\nYNY\nNYN\n', '2\r\n'),
        edge('4\nNYYN\nYNNN\nYNNY\nNNYN\n', '3\r\n'),
        edge('5\nNYYYY\nYNNNN\nYNNNN\nYNNNN\nYNNNN\n', '4\r\n'),
        stress('6\nNYNNNN\nYNYNNN\nNYNYNN\nNNYNYN\nNNNYNY\nNNNNYN\n', '4\r\n'),
    ]
