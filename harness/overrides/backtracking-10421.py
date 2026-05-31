from __future__ import annotations
import itertools
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    sizes = list(map(int, lines[1].split()))
    digs = lines[3].split()

    def ok(num: int, length: int) -> bool:
        text = str(num)
        return len(text) == length and all(ch in digs for ch in text)

    answer = 0
    for a_digits in itertools.product(digs, repeat=sizes[0]):
        a = int("".join(a_digits))
        for b_digits in itertools.product(digs, repeat=sizes[1]):
            b = int("".join(b_digits))
            rev = str(b)[::-1]
            if all(ok(a * int(rev[i]), sizes[2 + i]) for i in range(sizes[1])) and ok(a * b, sizes[-1]):
                answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("5\n3 2 3 3 4\n5\n2 3 4 6 8\n"),
        edge("6\n3 3 3 3 3 5\n6\n1 2 3 4 5 9\n"),
        stress("5\n2 1 2 3 3\n3\n1 2 3\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
