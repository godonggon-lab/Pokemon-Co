from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def _solve(stdin: str) -> str:
    lines = stdin.splitlines()
    poem = lines[0]
    space = int(lines[1])
    counts = list(map(int, lines[2].split()))

    def use_text(text: str) -> bool:
        prev = ""
        for ch in text:
            if ch == " ":
                continue
            lower = ch.lower()
            if lower == prev:
                continue
            idx = ord(lower) - 97
            counts[idx] -= 1
            if counts[idx] < 0:
                return False
            prev = lower
        return True

    title = "".join(word[0].upper() for word in poem.split())
    if poem.count(" ") > space or not use_text(poem) or not use_text(title):
        return "-1"
    return title


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    enough = " ".join(["10"] * 26)
    inputs = [
        f"There is no cow level\n4\n{enough}\n",
        f"aa aa\n1\n{enough}\n",
        "hello world\n0\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
        "abc\n0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
