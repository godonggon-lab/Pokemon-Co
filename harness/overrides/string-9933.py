from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    words = lines[1 : 1 + n]
    seen = set(words)
    for word in words:
        if word[::-1] in seen:
            return f"{len(word)} {word[len(word) // 2]}"
    raise AssertionError("problem input must contain an answer")


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "4\nlas\ngod\npsala\nsal\n",
        "2\nabc\ncba\n",
        "3\naaa\nbbb\nccc\n",
        "5\nhello\nworld\nlevel\npython\njudge\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    words = [f"word{i}" for i in range(50)] + ["abcde", "edcba"]
    stdin = f"{len(words)}\n" + "\n".join(words) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
