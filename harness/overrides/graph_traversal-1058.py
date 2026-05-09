from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nN\n"),
        edge("2\nNY\nYN\n"),
        edge("3\nNYN\nYNY\nNYN\n"),
        edge("4\nNYYN\nYNNN\nYNNY\nNNYN\n"),
        edge("5\nNYYYY\nYNNNN\nYNNNN\nYNNNN\nYNNNN\n"),
        stress("6\nNYNNNN\nYNYNNN\nNYNYNN\nNNYNYN\nNNNYNY\nNNNNYN\n"),
    ]
