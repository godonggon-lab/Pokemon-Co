from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    ident = "\n".join(" ".join("10" if i == j else "0" for j in range(11)) for i in range(11))
    shifted = "\n".join(" ".join("9" if j == (i + 1) % 11 else ("5" if j == i else "0") for j in range(11)) for i in range(11))
    return [edge("1\n" + ident + "\n"), stress("1\n" + shifted + "\n")]
