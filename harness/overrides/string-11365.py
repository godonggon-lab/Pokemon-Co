from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("END\n"),
        edge("abc\nEND\n"),
        edge("hello world\nEND\n"),
        edge("madam\nracecar\nEND\n"),
        edge("12345\n!@# $\nEND\n"),
        stress("DongJun CodeDex\nboj override\nEND\n"),
    ]
