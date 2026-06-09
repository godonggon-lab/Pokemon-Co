from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    prefix, suffix = lines[1].split("*")
    out = []
    for text in lines[2:2 + n]:
        ok = len(text) >= len(prefix) + len(suffix) and text.startswith(prefix) and text.endswith(suffix)
        out.append("DA" if ok else "NE")
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3\na*d\nabcd\nanestonestod\nfacebook\n"),
        edge("4\nab*cd\nabcd\nabxcd\nabdc\nxabcd\n"),
        edge("3\n*a\na\nba\nab\n"),
        edge("3\na*\na\nab\nba\n"),
        edge("3\nabc*xyz\nabcxyz\nabc123xyz\nabcxy\n"),
        stress("5\nx*y\nxy\nxay\nxxxy\nxabc\nabcy\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
