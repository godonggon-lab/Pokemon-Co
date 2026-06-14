from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _next(word: str) -> str:
    arr = list(word)
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i < 0:
        return word
    j = len(arr) - 1
    while arr[i] >= arr[j]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1 :] = reversed(arr[i + 1 :])
    return "".join(arr)


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    return "\n".join(_next(word) for word in lines[1 : 1 + int(lines[0])])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3\nHELLO\nDRINK\nSHUTTLE\n",
        "4\nABC\nCBA\nAAB\nABA\n",
        "2\nZ\nAZBY\n",
        "3\nA\nAA\nAB\n",
        "4\nBA\nBB\nBBA\nFEDCBA\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    words = ["ABCDE", "EDCBA", "AABBCC", "ABDC", "ZYXWV"] * 10
    stdin = f"{len(words)}\n" + "\n".join(words) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
