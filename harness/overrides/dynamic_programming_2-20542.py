from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 3\nabc\nabc\n"), edge("4 4\nilvj\njvli\n"), stress("5 6\nilabc\njlabbc\n")]
