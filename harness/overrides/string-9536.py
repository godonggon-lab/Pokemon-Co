from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    t = int(lines[0])
    idx = 1
    answers: list[str] = []
    for _ in range(t):
        recorded = lines[idx].split()
        idx += 1
        known: set[str] = set()
        while lines[idx] != "what does the fox say?":
            known.add(lines[idx].split()[-1])
            idx += 1
        idx += 1
        answers.append(" ".join(sound for sound in recorded if sound not in known))
    return "\n".join(answers)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\ntoot woof wa ow ow ow pa blub blub pa toot pa blub pa pa ow pow toot\n"
        "dog goes woof\nfish goes blub\nelephant goes toot\nseal goes ow\nwhat does the fox say?\n",
        "2\na b c d\nx goes b\ny goes d\nwhat does the fox say?\nmeow bark meow\ncat goes meow\nwhat does the fox say?\n",
        "1\nring ding ring\nbell goes dong\nwhat does the fox say?\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    recorded = " ".join(["fox"] * 20 + ["dog"] * 20 + ["cat"] * 20)
    stdin = f"1\n{recorded}\ndog goes dog\ncat goes cat\nwhat does the fox say?\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
