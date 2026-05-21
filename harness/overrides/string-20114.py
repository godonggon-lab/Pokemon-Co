from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def _solve(stdin: str) -> str:
    lines = stdin.strip("\n").splitlines()
    n, h, w = map(int, lines[0].split())
    rows = lines[1 : 1 + h]
    answer: list[str] = []
    for idx in range(n):
        found = "?"
        for row in rows:
            for ch in row[idx * w : (idx + 1) * w]:
                if ch != "?":
                    found = ch
                    break
            if found != "?":
                break
        answer.append(found)
    return "".join(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3 2 2\n?a????\n??b?c?\n",
        "5 1 1\nabcde\n",
        "4 3 2\n????????\n?a??b???\n??????z?\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
