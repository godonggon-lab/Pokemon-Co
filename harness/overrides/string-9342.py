from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nAFC\n"),
        edge("2\nAAFFCC\nBAFCC\n"),
        edge("3\nAFC\nAFFCC\nAAFCCB\n"),
        edge("4\nXYZ\nAAFC\nAAFCCC\nFAFC\n"),
        edge("5\nAFFFFCC\nCAAFFCC\nAAFFFCCC\nBAAAFFFC\nAAAFCCCD\n"),
        stress("6\nAFC\nBAFC\nAFFFCCCC\nDAFC\nEAAFFCCF\nGAFCC\n"),
    ]
