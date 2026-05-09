from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("A\nB\nC\nD\nE\n"),
        edge("ABCDE\nabcde\n12345\nVWXYZ\n!!!!!\n"),
        edge("AABCDD\nafzz\n09121\na8EWg6\nP5h3kx\n"),
        edge("short\nlonger\nmid\nx\nabcdefghi\n"),
        edge("123\n4567\n89\n0\nabcde\n"),
        stress("ABCDEFGHIJKLMNO\nabcdefghijklmno\n123456789012345\n!!!!!!!!!!!!!!!\nzzzzzzzzzzzzzzz\n"),
    ]
