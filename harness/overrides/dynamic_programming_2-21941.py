from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("abc\n1\nab 5\n"),
        edge("aaaa\n2\na 3\naa 10\n"),
        stress("banana\n3\nba 5\nna 4\nbanana 20\n"),
    ]
