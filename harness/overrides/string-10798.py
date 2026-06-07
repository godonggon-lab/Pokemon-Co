from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('A\nB\nC\nD\nE\n', 'ABCDE\r\n'),
        edge('ABCDE\nabcde\n12345\nVWXYZ\n!!!!!\n', 'Aa1V!Bb2W!Cc3X!Dd4Y!Ee5Z!\r\n'),
        edge('AABCDD\nafzz\n09121\na8EWg6\nP5h3kx\n', 'Aa0aPAf985Bz1EhCz2W3D1gkD6x\r\n'),
        edge('short\nlonger\nmid\nx\nabcdefghi\n', 'slmxahoibondcrgdteerfghi\r\n'),
        edge('123\n4567\n89\n0\nabcde\n', '1480a259b36c7de\r\n'),
        stress('ABCDEFGHIJKLMNO\nabcdefghijklmno\n123456789012345\n!!!!!!!!!!!!!!!\nzzzzzzzzzzzzzzz\n', 'Aa1!zBb2!zCc3!zDd4!zEe5!zFf6!zGg7!zHh8!zIi9!zJj0!zKk1!zLl2!zMm3!zNn4!zOo5!z\r\n'),
    ]
