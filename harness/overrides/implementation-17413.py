from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('baekjoon online judge\n', 'noojkeab enilno egduj\r\n'),
        edge('<open>tag<close>\n', '<open>gat<close>\r\n'),
        edge('<a>bc def<g>hi\n', '<a>cb fed<g>ih\r\n'),
        edge('one two three\n', 'eno owt eerht\r\n'),
        edge('<tag>word inside<tag2> tail\n', '<tag>drow edisni<tag2> liat\r\n'),
        stress('abc<def ghi>jkl mno<p>qr st\n', 'cba<def ghi>lkj onm<p>rq ts\r\n'),
    ]
