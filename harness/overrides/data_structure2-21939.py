from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 1\n1\nrecommend 1\n", "1\n"),
        edge("2\n1 1\n2 2\n2\nrecommend 1\nrecommend -1\n", "2\n1\n"),
        edge("2\n1 1\n2 2\n5\nadd 3 3\nrecommend 1\nsolved 3\nrecommend 1\nrecommend -1\n", "3\n2\n1\n"),
        edge("3\n10 5\n20 5\n30 1\n3\nrecommend 1\nrecommend -1\nsolved 20\n", "20\n30\n"),
        edge("2\n100 10\n200 20\n4\nadd 150 20\nrecommend 1\nsolved 200\nrecommend 1\n", "200\n150\n"),
        stress("3\n1 3\n2 3\n3 1\n6\nrecommend 1\nrecommend -1\nadd 4 5\nrecommend 1\nsolved 4\nrecommend 1\n", "2\n3\n4\n2\n"),
    ]
