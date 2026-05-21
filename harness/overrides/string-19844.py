from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge

PREFIXES = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"]
VOWELS = set("aeiouh")


def _solve(stdin: str) -> str:
    parts = stdin.strip().replace(" ", "-").split("-")
    answer = len(parts)
    for part in parts:
        for prefix in PREFIXES:
            if part.startswith(prefix) and len(part) > len(prefix) and part[len(prefix)] in VOWELS:
                answer += 1
                break
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "l'amour est bleu\n",
        "qu'il-est-bon\n",
        "bonjour le monde\n",
        "c'est-difficile d'apprendre\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
