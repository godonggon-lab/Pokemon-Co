from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("baekjoon online judge\n"),
        edge("<open>tag<close>\n"),
        edge("<a>bc def<g>hi\n"),
        edge("one two three\n"),
        edge("<tag>word inside<tag2> tail\n"),
        stress("abc<def ghi>jkl mno<p>qr st\n"),
    ]
