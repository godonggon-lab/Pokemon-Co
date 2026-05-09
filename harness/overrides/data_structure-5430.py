from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nR\n0\n[]\n", "[]\n"),
        edge("1\nD\n0\n[]\n", "error\n"),
        edge("1\nD\n1\n[1]\n", "[]\n"),
        edge("1\nR\n3\n[1,2,3]\n", "[3,2,1]\n"),
        edge("1\nRDD\n4\n[1,2,3,4]\n", "[2,1]\n"),
        stress("2\nDD\n1\n[42]\nRDRD\n4\n[1,2,3,4]\n", "error\n[2,3]\n"),
    ]
