from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    answer = temp = ""
    in_tag = False
    for ch in stdin.rstrip("\n"):
        if ch == "<":
            answer += temp[::-1]
            temp = ""
            in_tag = True
            answer += ch
        elif ch == ">":
            in_tag = False
            answer += ch
        elif in_tag:
            answer += ch
        elif ch == " ":
            answer += temp[::-1] + " "
            temp = ""
        else:
            temp += ch
    return answer + temp[::-1] + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["baekjoon online judge\n", "<open>tag<close>\n", "<a>bc def<g>hi\n", "one two three\n", "<tag>word inside<tag2> tail\n", "abc<def ghi>jkl mno<p>qr st\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
