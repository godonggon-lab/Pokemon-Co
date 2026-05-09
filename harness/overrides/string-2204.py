from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nApple\n0\n"),
        edge("2\nbanana\nApple\n0\n"),
        edge("3\nZoo\nalpha\nBeta\n0\n"),
        edge("4\nabc\nAbd\naba\nAAA\n0\n"),
        edge("2\nsame\nSame\n3\nx\nY\nz\n0\n"),
        stress("5\nDelta\ncharlie\nbravo\nAlpha\necho\n0\n"),
    ]
