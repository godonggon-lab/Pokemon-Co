from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\nA\n"),
        edge("2 4\nAAAA\nTTTT\n"),
        edge("3 5\nAAAAA\nAACAA\nAAGAA\n"),
        edge("4 6\nTATATA\nTATATA\nCCCCCC\nGGGGGG\n"),
        edge("5 8\nACGTACGT\nACGTTCGT\nACGTACGA\nTCGTACGT\nACGTACGT\n"),
        stress("6 10\nAAAAAAAAAA\nCCCCCCCCCC\nGGGGGGGGGG\nTTTTTTTTTT\nACGTACGTAC\nTGCATGCATG\n"),
    ]
