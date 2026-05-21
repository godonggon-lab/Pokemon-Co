from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\nab\ncd\n"),
        edge("3\naa\nab\ncc\n"),
        edge("4\nfoo\napp\nbar\nbaz\n"),
        edge("5\nabc\nbcd\naba\nxyx\nzzz\n"),
        stress("10\n" + "\n".join(["abc", "bcd", "cde", "aba", "xyx", "zzz", "abb", "cdd", "qwe", "rty"]) + "\n"),
    ]
