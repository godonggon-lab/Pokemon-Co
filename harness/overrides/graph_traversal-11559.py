from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    empty = "\n".join(["......"]*12) + "\n"
    one = "\n".join(["......"]*11 + ["RRRR.."]) + "\n"
    return [edge(empty), edge(one), stress("\n".join(["......"]*8 + ["YYYY..","YYYY..","RRRR..","RRRR.."]) + "\n")]
