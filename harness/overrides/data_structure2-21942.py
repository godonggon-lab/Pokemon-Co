from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 001/00:01 10\n2021-01-01 00:00 part alice\n"),
        edge("2 001/00:01 10\n2021-01-01 00:00 part alice\n2021-01-01 00:01 part alice\n"),
        edge("2 000/00:01 100\n2021-01-01 00:00 lens bob\n2021-01-01 00:03 lens bob\n"),
        edge("4 001/00:00 5\n2021-01-01 00:00 a kim\n2021-01-01 00:30 a kim\n2021-01-01 01:00 b lee\n2021-01-03 01:01 b lee\n"),
        edge("5 000/00:10 2\n2021-01-01 00:00 p a\n2021-01-01 00:20 p a\n2021-01-01 00:00 q b\n2021-01-01 00:09 q b\n2021-01-02 00:00 r c\n"),
        stress("6 001/12:00 3\n2021-01-01 00:00 x aa\n2021-01-02 13:00 x aa\n2021-01-01 00:00 y bb\n2021-01-01 12:00 y bb\n2021-01-03 00:00 z cc\n2021-01-05 00:01 z cc\n"),
    ]
