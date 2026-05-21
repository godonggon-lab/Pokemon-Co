from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    s = lines[0]
    prefix = [[0] * 26]
    for ch in s:
        row = prefix[-1][:]
        row[ord(ch) - 97] += 1
        prefix.append(row)
    q = int(lines[1])
    out: list[str] = []
    for line in lines[2 : 2 + q]:
        a, l_s, r_s = line.split()
        l = int(l_s)
        r = int(r_s)
        idx = ord(a) - 97
        out.append(str(prefix[r + 1][idx] - prefix[l][idx]))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "seungjaehwang\n4\na 0 5\na 0 6\na 6 10\na 7 10\n",
        "abcabc\n3\na 0 5\nb 1 4\nc 2 2\n",
        "aaaaa\n2\na 0 4\nb 0 4\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "abcdefghijklmnopqrstuvwxyz" * 100
    queries = [f"{chr(97 + i % 26)} 0 {len(s) - 1}" for i in range(100)]
    stdin = s + "\n" + str(len(queries)) + "\n" + "\n".join(queries) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
