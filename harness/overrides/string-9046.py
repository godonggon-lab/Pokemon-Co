from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\na\n"),
        edge("1\naabb\n"),
        edge("2\nhello world\nmississippi\n"),
        edge("3\nabc abc\nzzzz y\none two three\n"),
        edge("4\na\na a a b\nx y z\nmmmmnn\n"),
        stress("5\ndongjun codedex\nalgorithm problem solving\nbanana bandana\nabcde\nzzzzzzzz\n"),
    ]
