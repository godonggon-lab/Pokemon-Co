from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1 1\nSE\n..\n"),
        edge("3 1 1\nS..\n...\n..E\n"),
        edge("3 2 1\nS.U\n...\n..E\n"),
        edge("4 2 2\nS...\n.U..\n..U.\n...E\n"),
        edge("5 3 1\nS....\nUUUU.\n.....\n.UUUU\n....E\n"),
        edge("5 1 3\nS....\n.....\n..U..\n.....\n....E\n"),
        stress("7 3 2\nS..U...\n.......\n..U....\n.......\n....U..\n.......\n......E\n"),
    ]
