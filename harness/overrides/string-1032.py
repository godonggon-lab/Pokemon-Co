from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nabc\n"),
        edge("2\nabc\nabc\n"),
        edge("2\nabc\nabd\n"),
        edge("3\nconfig.sys\nconfig.inf\nconfigures\n"),
        edge("4\nabcd\naXcd\nabYd\nabcZ\n"),
        stress("5\nhello\nhallo\nhullo\nhxllo\nhello\n"),
    ]
