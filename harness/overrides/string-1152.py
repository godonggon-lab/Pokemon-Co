from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("word\n"),
        edge(" hello world \n"),
        edge("   \n"),
        edge("a b c d e\n"),
        edge("  multiple   spaces  inside  \n"),
        stress("The Curious Case Of DongJun CodeDex\n"),
    ]
