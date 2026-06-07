from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\na\n', 'a\r\n'),
        edge('3\nb\na\nc\n', 'a\r\nb\r\nc\r\n'),
        edge('5\nword\nword\na\nab\nabc\n', 'a\r\nab\r\nabc\r\nword\r\n'),
        edge('6\nbanana\napple\napp\napply\nbat\nbar\n', 'app\r\nbar\r\nbat\r\napple\r\napply\r\nbanana\r\n'),
        edge('7\nz\nyy\nxxx\nwwww\nvv\nu\nttt\n', 'u\r\nz\r\nvv\r\nyy\r\nttt\r\nxxx\r\nwwww\r\n'),
        stress('10\nhello\nhi\nh\nworld\nword\nalgorithm\nalgo\ncode\ncoder\ncode\n', 'h\r\nhi\r\nalgo\r\ncode\r\nword\r\ncoder\r\nhello\r\nworld\r\nalgorithm\r\n'),
    ]
