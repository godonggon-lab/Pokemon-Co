from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 5\na\nb\n', 'a___b\r\n'),
        edge('3 10\nA\nb\nC\n', 'A____b___C\r\n'),
        edge('4 20\nhello\nWorld\nabc\nDef\n', 'hello_World__abc_Def\r\n'),
        edge('3 12\naa\nbb\ncc\n', 'aa___bb___cc\r\n'),
        stress('5 30\nAlpha\nbeta\nGamma\ndelta\nEpsilon\n', 'Alpha_beta_Gamma_delta_Epsilon\r\n'),
    ]
