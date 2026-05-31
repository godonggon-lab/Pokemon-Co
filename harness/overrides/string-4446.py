from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress

VOWELS = "aiyeou"
CONSONANTS = "bkxznhdcwgpvjqtsrlmf"


def _solve(stdin: str) -> str:
    out: list[str] = []
    for line in stdin.splitlines():
        chars: list[str] = []
        for ch in line:
            lower = ch.lower()
            if lower in VOWELS:
                nxt = VOWELS[(VOWELS.index(lower) + 3) % len(VOWELS)]
                chars.append(nxt.upper() if ch.isupper() else nxt)
            elif lower in CONSONANTS:
                nxt = CONSONANTS[(CONSONANTS.index(lower) + 10) % len(CONSONANTS)]
                chars.append(nxt.upper() if ch.isupper() else nxt)
            else:
                chars.append(ch)
        out.append("".join(chars))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "Ita dotf ni dyca nsaw ecc.\n",
        "AiYeOu BKXZNHDCWGPVJQTSRLMF\n",
        "123 !?~\nIta\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    hard = "Dip dip dip clap stomp clap\njiggle dip hop twirl clap stomp clap\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
