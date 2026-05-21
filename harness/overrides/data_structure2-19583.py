from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    start, end, quit_time = lines[0].split()
    before: set[str] = set()
    after: set[str] = set()
    for line in lines[1:]:
        time, name = line.split()
        if time <= start:
            before.add(name)
        elif end <= time <= quit_time:
            after.add(name)
    return str(len(before & after))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "22:00 23:00 23:30\n21:59 a\n22:00 b\n23:00 a\n23:31 b\n23:20 b\n",
        "09:00 10:00 11:00\n08:59 anna\n10:30 anna\n10:30 bob\n",
        "12:00 13:00 14:00\n12:01 late\n13:30 late\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
