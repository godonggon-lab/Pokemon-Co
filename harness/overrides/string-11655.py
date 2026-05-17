from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.rstrip("\n")
    out: list[str] = []
    for ch in s:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - ord("a") + 13) % 26 + ord("a")))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - ord("A") + 13) % 26 + ord("A")))
        else:
            out.append(ch)
    return "".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "Baekjoon Online Judge\n",
        "One is 1\n",
        "abcdefghijklmnopqrstuvwxyz\n",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n",
        "1234 !?\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "AbcXyz 0123! " * 100
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
