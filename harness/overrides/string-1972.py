from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _is_surprising(s: str) -> bool:
    for d in range(1, len(s)):
        seen: set[str] = set()
        for i in range(len(s) - d):
            pair = s[i] + s[i + d]
            if pair in seen:
                return False
            seen.add(pair)
    return True


def _solve(stdin: str) -> str:
    out: list[str] = []
    for line in stdin.splitlines():
        s = line.strip()
        if s == "*":
            break
        out.append(f"{s} is {'surprising' if _is_surprising(s) else 'NOT surprising'}.")
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "ZGBG\nX\nEE\nAAB\nAABA\nAABB\nBCBABCC\n*\n",
        "A\nAB\nABC\nABCA\n*\n",
        "AAAA\nABCDE\n*\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    words = ["".join(chr(65 + ((i + j * 7) % 26)) for i in range(20)) for j in range(30)]
    stdin = "\n".join(words + ["*"]) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
