from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\na*d\nabcd\nanestonestod\nfacebook\n"), edge("4\nab*cd\nabcd\nabxcd\nabdc\nxabcd\n"), stress("5\nx*y\nxy\nxay\nxxxy\nxabc\nabcy\n")]
