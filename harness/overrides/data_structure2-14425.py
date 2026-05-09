from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\na\na\n", "1\n"),
        edge("1 1\na\nb\n", "0\n"),
        edge("3 4\na\nb\nc\na\nc\nd\nb\n", "3\n"),
        edge("3 3\nhello\nworld\nhi\nhell\nhello\nworld\n", "2\n"),
        edge("5 5\nA\nB\nC\nD\nE\nE\nD\nX\nA\nY\n", "3\n"),
        stress("6 8\nred\nblue\ngreen\nyellow\nblack\nwhite\nred\npink\nwhite\nblue\nblack\ngray\ngreen\ncyan\n", "5\n"),
    ]
