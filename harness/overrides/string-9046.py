from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\na\n', 'a\r\n'),
        edge('1\naabb\n', '?\r\n'),
        edge('2\nhello world\nmississippi\n', 'l\r\n?\r\n'),
        edge('3\nabc abc\nzzzz y\none two three\n', '?\r\nz\r\ne\r\n'),
        edge('4\na\na a a b\nx y z\nmmmmnn\n', 'a\r\na\r\n?\r\nm\r\n'),
        stress('5\ndongjun codedex\nalgorithm problem solving\nbanana bandana\nabcde\nzzzzzzzz\n', 'd\r\n?\r\na\r\n?\r\nz\r\n'),
    ]
