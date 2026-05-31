from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, _m = map(int, lines[0].split())
    rows = lines[1 : 1 + n]
    k = int(lines[1 + n])
    answer = 0
    for row in rows:
        zeros = row.count("0")
        if zeros <= k and (k - zeros) % 2 == 0:
            answer = max(answer, rows.count(row))
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3 2\n01\n10\n10\n1\n",
        "4 3\n000\n000\n111\n010\n2\n",
        "2 4\n1111\n1111\n3\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    rows = ["0101010101" if i % 2 else "1010101010" for i in range(20)]
    hard = "20 10\n" + "\n".join(rows) + "\n5\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
