from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1 A\n', 'A\r\n'),
        edge('3\n2 A B\n2 A C\n1 D\n', 'A\r\n--B\r\n--C\r\nD\r\n'),
        edge('2\n1 B\n1 A\n', 'A\r\nB\r\n'),
        edge('3\n1 A\n2 A B\n3 A B C\n', 'A\r\n--B\r\n----C\r\n'),
        edge('4\n2 A C\n2 A B\n2 B A\n2 B C\n', 'A\r\n--B\r\n--C\r\nB\r\n--A\r\n--C\r\n'),
        stress('4\n3 KIWI APPLE BANANA\n2 KIWI APPLE\n3 KIWI ORANGE PEAR\n1 APPLE\n', 'APPLE\r\nKIWI\r\n--APPLE\r\n----BANANA\r\n--ORANGE\r\n----PEAR\r\n'),
    ]
