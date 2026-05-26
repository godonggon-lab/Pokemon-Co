from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2\nred\nblue\nfish\nbird\n3\nredfish\nbluebird\nredbird\n"),
        stress("3 3\na\nab\nabc\nx\nbc\nc\n5\nax\nabc\nabcx\nabbc\nabz\n"),
    ]
