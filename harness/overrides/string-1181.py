from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\na\n"),
        edge("3\nb\na\nc\n"),
        edge("5\nword\nword\na\nab\nabc\n"),
        edge("6\nbanana\napple\napp\napply\nbat\nbar\n"),
        edge("7\nz\nyy\nxxx\nwwww\nvv\nu\nttt\n"),
        stress("10\nhello\nhi\nh\nworld\nword\nalgorithm\nalgo\ncode\ncoder\ncode\n"),
    ]
