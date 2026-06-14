from __future__ import annotations

import re
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    source = stdin.strip()
    main = re.search(r"<main>(.*)</main>", source).group(1)
    out: list[str] = []
    for title, body in re.findall(r'<div title="(.*?)">(.*?)</div>', main):
        out.append(f"title : {title}")
        for paragraph in re.findall(r"<p>(.*?)</p>", body):
            text = re.sub(r"<.*?>", "", paragraph)
            text = re.sub(r"\s+", " ", text.strip())
            out.append(text)
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        '<main><div title="title_name_1"><p>paragraph 1</p><p>paragraph 2</p></div></main>\n',
        '<main><div title="A"><p> hello   <b>world</b> </p></div><div title="B"><p><i>x</i>  y</p></div></main>\n',
        '<main><div title="empty"><p>   many     spaces   </p></div></main>\n',
        '<main><div title="one"><p>x</p></div></main>\n',
        '<main><div title="nested"><p><b><i>deep</i></b> text</p><p>a     b</p></div></main>\n',
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    hard = '<main><div title="A"><p> alpha   <b>beta</b> gamma </p><p><i>delta</i></p></div><div title="B"><p>one <span>two</span> three</p></div></main>\n'
    cases.append(stress(hard, _solve(hard)))
    return cases
