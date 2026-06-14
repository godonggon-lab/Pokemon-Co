from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\nA\nB\nC\n', 'ABC\r\n'),
        edge('6\nA\nC\nD\nB\nC\nB\n', 'ABCBCD\r\n'),
        edge('1\nZ\n', 'Z\r\n'),
        edge('4\nD\nC\nB\nA\n', 'ABCD\r\n'),
        edge('5\nA\nB\nC\nB\nA\n', 'AABBC\r\n'),
        stress('100\nA\nH\nO\nV\nC\nJ\nQ\nX\nE\nL\nS\nZ\nG\nN\nU\nB\nI\nP\nW\nD\nK\nR\nY\nF\nM\nT\nA\nH\nO\nV\nC\nJ\nQ\nX\nE\nL\nS\nZ\nG\nN\nU\nB\nI\nP\nW\nD\nK\nR\nY\nF\nM\nT\nA\nH\nO\nV\nC\nJ\nQ\nX\nE\nL\nS\nZ\nG\nN\nU\nB\nI\nP\nW\nD\nK\nR\nY\nF\nM\nT\nA\nH\nO\nV\nC\nJ\nQ\nX\nE\nL\nS\nZ\nG\nN\nU\nB\nI\nP\nW\nD\nK\nR\n', 'AHORKDVCJQWPIBUNGXELSZGNUBIPWDKRYFMTAHOVCJQXELSZGNUBIPWDKRYFMTAHOVCJQXELSZGNUBIP\r\nWDKRYFMTAHOVCJQXELSZ\r\n'),
    ]
