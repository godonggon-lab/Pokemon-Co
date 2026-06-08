from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    text = data.strip()
    vowels = set("AEIOU")
    answer = 0

    def dfs(index: int, vowel_run: int, consonant_run: int, has_l: bool, multiplier: int) -> None:
        nonlocal answer
        if vowel_run >= 3 or consonant_run >= 3:
            return
        if index == len(text):
            if has_l:
                answer += multiplier
            return
        char = text[index]
        if char == "_":
            dfs(index + 1, vowel_run + 1, 0, has_l, multiplier * 5)
            dfs(index + 1, 0, consonant_run + 1, True, multiplier)
            dfs(index + 1, 0, consonant_run + 1, has_l, multiplier * 20)
        elif char in vowels:
            dfs(index + 1, vowel_run + 1, 0, has_l, multiplier)
        else:
            dfs(index + 1, 0, consonant_run + 1, has_l or char == "L", multiplier)

    dfs(0, 0, 0, False, 1)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("L\n"), edge("_\n"), edge("A\n"), edge("LL\n"), edge("__L\n"), stress("A__L_B\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
