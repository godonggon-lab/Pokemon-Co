from __future__ import annotations

from collections import Counter
from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    counts = Counter(name.split(".")[-1] for name in lines[1:])
    return "".join(f"{ext} {counts[ext]}\n" for ext in sorted(counts))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\na.txt\n", "3\na.txt\nb.txt\nc.py\n", "5\na.cpp\nb.py\nc.cpp\nd.java\ne.py\n", "4\nfoo.a\nbar.b\nbaz.a\nqux.c\n", "6\none.tar\ntwo.gz\nthree.tar\nfour.zip\nfive.gz\nsix.gz\n", "8\na.x\nb.y\nc.x\nd.z\ne.y\nf.x\ng.z\nh.z\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
