from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def ok(word: str) -> bool:
    vowels = set("aeiou")
    has_vowel = False
    v_count = c_count = 0
    prev = ""
    for ch in word:
        if ch in vowels:
            has_vowel = True
            v_count += 1
            c_count = 0
        else:
            c_count += 1
            v_count = 0
        if v_count == 3 or c_count == 3:
            return False
        if ch == prev and ch not in "eo":
            return False
        prev = ch
    return has_vowel


def expected(stdin: str) -> str:
    out = []
    for word in stdin.strip().splitlines():
        if word == "end":
            break
        out.append(f"<{word}> is {'acceptable' if ok(word) else 'not acceptable'}.")
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["a\nend\n", "tv\nptoui\nbontres\nzoggax\nwiinq\neep\nhouctuh\nend\n", "aaa\nabc\nabcd\nend\n", "ee\noo\naa\nend\n", "hello\nworld\nqueue\nend\n", "aeiou\nxyz\nbook\nend\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
