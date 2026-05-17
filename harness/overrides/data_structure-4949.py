from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _is_balanced(line: str) -> bool:
    stack: list[str] = []
    pairs = {")": "(", "]": "["}
    for ch in line:
        if ch in "([":
            stack.append(ch)
        elif ch in ")]":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def _solve(stdin: str) -> str:
    out: list[str] = []
    for line in stdin.splitlines():
        if line == ".":
            break
        out.append("yes" if _is_balanced(line) else "no")
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        ".\n",
        "()[]\n.\n",
        "([)]\n.\n",
        "So when I die (the [first] I will see in (heaven) is a score list).\n.\n",
        "([[[[]]]])\n([[[[]]])\n.\n",
        "no brackets here\n([text] (more text))\n([text] (more text)]\n.\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]

    many = "\n".join(["([])" * 20, "([)]" * 20, "(" * 50 + ")" * 50, "."]) + "\n"
    cases.append(stress(many, _solve(many)))
    return cases
