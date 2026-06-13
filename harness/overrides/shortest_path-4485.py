from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n5\n0\n', 'Problem 1: 5\r\n'),
        edge('3\n5 5 4\n3 9 1\n3 2 7\n0\n', 'Problem 1: 20\r\n'),
        edge('2\n1 1\n1 1\n0\n', 'Problem 1: 3\r\n'),
        edge('3\n1 100 1\n1 100 1\n1 1 1\n0\n', 'Problem 1: 5\r\n'),
        edge('2\n1 2\n3 4\n2\n9 9\n9 9\n0\n', 'Problem 1: 7\r\nProblem 2: 27\r\n'),
        stress('5\n1 2 3 4 5\n1 3 5 7 9\n1 4 7 1 4\n1 5 9 4 8\n1 6 2 7 3\n0\n', 'Problem 1: 23\r\n'),
    ]
