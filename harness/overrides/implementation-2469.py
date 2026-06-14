from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    k = int(lines[0])
    n = int(lines[1])
    target = list(lines[2])
    ladder = lines[3 : 3 + n]
    top = [chr(ord("A") + i) for i in range(k)]
    unknown = ladder.index("?" * (k - 1))
    for line in ladder[:unknown]:
        for i, ch in enumerate(line):
            if ch == "-":
                top[i], top[i + 1] = top[i + 1], top[i]
    bottom = target[:]
    for line in reversed(ladder[unknown + 1 :]):
        for i, ch in enumerate(line):
            if ch == "-":
                bottom[i], bottom[i + 1] = bottom[i + 1], bottom[i]
    answer = ["*"] * (k - 1)
    i = 0
    possible = True
    while i < k - 1:
        if top[i] == bottom[i]:
            i += 1
        elif top[i] == bottom[i + 1] and top[i + 1] == bottom[i]:
            answer[i] = "-"
            top[i], top[i + 1] = top[i + 1], top[i]
            i += 2
        else:
            possible = False
            break
    if top[-1] != bottom[-1]:
        possible = False
    return "".join(answer) if possible else "x" * (k - 1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "4\n3\nBACD\n***\n???\n***\n",
        "5\n5\nACBED\n*-**\n****\n????\n-***\n**-*\n",
        "3\n2\nCBA\n??\n**\n",
        "2\n1\nAB\n?\n",
        "4\n2\nABCD\n???\n***\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    hard = "6\n6\nFABCDE\n-****\n*-***\n?????\n**-**\n***-*\n****-\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
