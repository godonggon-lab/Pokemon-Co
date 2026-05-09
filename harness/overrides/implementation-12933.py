from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    sound = stdin.strip()
    order = "quack"
    used = [False] * len(sound)
    ducks = 0
    while True:
        idx = 0
        found = False
        for i, ch in enumerate(sound):
            if not used[i] and ch == order[idx]:
                used[i] = True
                idx += 1
                if idx == 5:
                    found = True
                    idx = 0
        if idx != 0:
            return "-1\n"
        if not found:
            break
        ducks += 1
    return f"{ducks}\n" if ducks and all(used) else "-1\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["quack\n", "quackquack\n", "qquuaacckk\n", "quqacukqauackck\n", "abc\n", "quackquackquack\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
