from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    unheard = set(lines[1:1 + n])
    both = sorted(name for name in lines[1 + n:1 + n + m] if name in unheard)
    return f"{len(both)}\n" + "".join(name + "\n" for name in both)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1 1\na\na\n", "2 2\na\nb\nc\nd\n", "3 4\nbaekjoon\nstartlink\ncodeplus\nbaekjoon\ncodeplus\ncodeminus\nstartlink\n", "3 3\nz\ny\nx\nx\ny\nz\n", "4 3\nkim\nlee\npark\nchoi\nchoi\ncho\nkim\n", "5 5\na\nb\nc\nd\ne\ne\nd\nc\nb\na\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
