from __future__ import annotations

import functools
from typing import List

from harness.cases import GeneratedCase, edge

ORDER = {ch: i for i, ch in enumerate("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")}


def _tokens(s: str) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            result.append(("num", s[i:j]))
            i = j
        else:
            result.append(("chr", s[i]))
            i += 1
    return result


def _cmp(a: str, b: str) -> int:
    ta, tb = _tokens(a), _tokens(b)
    for x, y in zip(ta, tb):
        if x[0] != y[0]:
            return -1 if x[0] == "num" else 1
        if x[0] == "chr":
            if x[1] != y[1]:
                return ORDER[x[1]] - ORDER[y[1]]
        else:
            ax = x[1].lstrip("0") or "0"
            by = y[1].lstrip("0") or "0"
            if len(ax) != len(by):
                return len(ax) - len(by)
            if ax != by:
                return -1 if ax < by else 1
            az = len(x[1]) - len(x[1].lstrip("0"))
            bz = len(y[1]) - len(y[1].lstrip("0"))
            if az != bz:
                return az - bz
    return len(ta) - len(tb)


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    arr = lines[1 : 1 + n]
    return "\n".join(sorted(arr, key=functools.cmp_to_key(_cmp)))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "5\nA1\nA01\na1\nA2\nA10\n",
        "6\nimg12\nimg0012\nimg2\nImg1\n1abc\nabc1\n",
        "4\nZ9\nz9\nA000\na0\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
