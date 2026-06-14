from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\nA B C\n2\nA B\nB C\n', '1\r\nC\r\nA 0\r\nB 1 A\r\nC 1 B\r\n'),
        edge('5\nkim lee park choi jung\n3\nlee kim\npark kim\nchoi lee\n', '2\r\njung kim\r\nchoi 0\r\njung 0\r\nkim 2 lee park\r\nlee 1 choi\r\npark 0\r\n'),
        edge('1\na\n0\n', '1\r\na\r\na 0\r\n'),
        edge('2\na b\n0\n', '2\r\na b\r\na 0\r\nb 0\r\n'),
        edge('4\na b c d\n3\nb a\nc b\nd c\n', '1\r\na\r\na 1 b\r\nb 1 c\r\nc 1 d\r\nd 0\r\n'),
        stress('6\na b c d e f\n5\nb a\nc a\nd b\ne b\nf c\n', '1\r\na\r\na 2 b c\r\nb 2 d e\r\nc 1 f\r\nd 0\r\ne 0\r\nf 0\r\n'),
    ]
