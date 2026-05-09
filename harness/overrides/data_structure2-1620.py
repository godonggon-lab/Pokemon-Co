from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 2\nPikachu\n1\nPikachu\n", "Pikachu\n1\n"),
        edge("2 4\nA\nB\n1\n2\nA\nB\n", "A\nB\n1\n2\n"),
        edge("3 3\nRed\nBlue\nGreen\n3\n1\nBlue\n", "Green\nRed\n2\n"),
        edge("4 4\nAA\nBB\nCC\nDD\nDD\nCC\nBB\nAA\n", "4\n3\n2\n1\n"),
        edge("5 5\nA1\nB2\nC3\nD4\nE5\n5\n4\n3\n2\n1\n", "E5\nD4\nC3\nB2\nA1\n"),
        stress("6 6\nAlpha\nBeta\nGamma\nDelta\nEpsilon\nZeta\nAlpha\n6\nGamma\n4\nEpsilon\n2\n", "1\nZeta\n3\nDelta\n5\nBeta\n"),
    ]
