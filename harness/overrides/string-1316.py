from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\na\n', '1\r\n'),
        edge('3\nhappy\nnew\nyear\n', '3\r\n'),
        edge('4\naba\nabab\nabcabc\na\n', '1\r\n'),
        edge('5\naa\nabca\nzzzz\nxyyx\nabc\n', '3\r\n'),
        edge('6\naabbcc\nabcabc\nabccba\nqwerty\nqqwwee\nqweq\n', '3\r\n'),
        stress('8\nabc\nabbc\nabca\nzzzzy\nzyxyz\nmnop\nmnoom\nppqqrr\n', '5\r\n'),
    ]
