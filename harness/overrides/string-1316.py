from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\na\n"),
        edge("3\nhappy\nnew\nyear\n"),
        edge("4\naba\nabab\nabcabc\na\n"),
        edge("5\naa\nabca\nzzzz\nxyyx\nabc\n"),
        edge("6\naabbcc\nabcabc\nabccba\nqwerty\nqqwwee\nqweq\n"),
        stress("8\nabc\nabbc\nabca\nzzzzy\nzyxyz\nmnop\nmnoom\nppqqrr\n"),
    ]
