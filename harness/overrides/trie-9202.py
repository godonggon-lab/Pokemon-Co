from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4\nGEEK\nFOR\nQUIZ\nGO\n1\nGIZU\nUEKQ\nQSEF\nORGO\n', '2 GEEK 3\r\n'),
        edge('3\nA\nAB\nABC\n1\nABCD\nEFGH\nIJKL\nMNOP\n', '1 ABC 3\r\n'),
        edge('1\nA\n1\nAAAA\nAAAA\nAAAA\nAAAA\n', '0 A 1\r\n'),
        edge('2\nCAT\nDOG\n1\nCATX\nXXXX\nDOGX\nXXXX\n', '2 CAT 2\r\n'),
        edge('1\nAAA\n1\nAAAA\nAAAA\nAAAA\nAAAA\n', '1 AAA 1\r\n'),
        stress('5\nTREE\nTRIE\nALGO\nCODE\nDOG\n2\nTREE\nAAAA\nCODE\nDOGS\nXXXX\nTRIE\nALGO\nCODE\nDOGX\n', '3 CODE 3\r\n4 ALGO 4\r\n'),
    ]
