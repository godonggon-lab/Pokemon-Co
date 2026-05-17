from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    if not s or s[0] == "_" or s[-1] == "_" or s[0].isupper() or "__" in s:
        return "Error!"
    has_under = "_" in s
    has_upper = any(ch.isupper() for ch in s)
    if has_under and has_upper:
        return "Error!"
    if has_under:
        parts = s.split("_")
        if any((not part) or (not part.islower()) for part in parts):
            return "Error!"
        return parts[0] + "".join(part.capitalize() for part in parts[1:])
    out: list[str] = []
    for ch in s:
        if ch.isupper():
            out.append("_")
            out.append(ch.lower())
        else:
            out.append(ch)
    return "".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "javaIdentifier\n",
        "long_and_mnemonic_identifier\n",
        "already\n",
        "_bad\n",
        "bad_\n",
        "bad__name\n",
        "Bad\n",
        "bad_Name\n",
        "bad_2name\n",
        "javaID\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "very_long_java_identifier_name_with_many_parts"
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
