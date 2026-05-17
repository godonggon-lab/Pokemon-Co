from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    plain, key = stdin.splitlines()[:2]
    out: list[str] = []
    for i, ch in enumerate(plain):
        if ch == " ":
            out.append(" ")
        else:
            shift = ord(key[i % len(key)]) - ord("a") + 1
            out.append(chr((ord(ch) - ord("a") - shift) % 26 + ord("a")))
    return "".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "nice day\nlove\n",
        "abc\nabc\n",
        "zzz\nz\n",
        "a b c\nabc\n",
        "hello world\nkey\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    plain = "the quick brown fox jumps over the lazy dog"
    stdin = plain + "\n" + "algorithm" + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
