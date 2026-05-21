from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    happy: list[int] = []
    tired: list[int] = []
    for line in lines[1 : 1 + n]:
        h, t = map(int, line.split())
        happy.append(h)
        tired.append(t)
    inf = 10**30
    pref_min_h = [inf] * n
    pref_max_t = [-inf] * n
    cur_h = inf
    cur_t = -inf
    for i in range(n):
        if happy[i]:
            cur_h = min(cur_h, happy[i])
        if tired[i]:
            cur_t = max(cur_t, tired[i])
        pref_min_h[i] = cur_h
        pref_max_t[i] = cur_t
    suf_max_h = [-inf] * n
    suf_min_t = [inf] * n
    cur_h = -inf
    cur_t = inf
    for i in range(n - 1, -1, -1):
        if happy[i]:
            cur_h = max(cur_h, happy[i])
        if tired[i]:
            cur_t = min(cur_t, tired[i])
        suf_max_h[i] = cur_h
        suf_min_t[i] = cur_t
    answer = -1
    for k in range(1, n):
        if pref_min_h[k - 1] > suf_max_h[k] and pref_max_t[k - 1] < suf_min_t[k]:
            answer = k
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "5\n5 1\n4 2\n3 3\n2 5\n1 4\n",
        "3\n1 1\n2 2\n3 3\n",
        "3\n0 0\n0 0\n0 0\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    rows = "\n".join(f"{1000 - i} {i + 1}" for i in range(100))
    stdin = f"100\n{rows}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
