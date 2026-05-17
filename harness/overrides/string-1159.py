from __future__ import annotations

from collections import Counter
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    counter = Counter(line[0] for line in lines[1:1 + n])
    answer = "".join(ch for ch in sorted(counter) if counter[ch] >= 5)
    return answer if answer else "PREDAJA"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\nalice\n",
        "5\napple\nangle\narea\narch\natom\n",
        "6\nbanana\nbrian\nbelle\nbetty\nbobby\nalice\n",
        "10\nalice\namy\nallen\nbrad\nbrian\nbella\ncarl\ncindy\nchris\nclaire\n",
        "15\nadam\nalex\nallen\narthur\namy\nbob\nbill\nben\nbrad\nbella\ncarl\ncody\nchris\nclaire\ncain\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    names = [f"{chr(97 + (i % 26))}name{i}" for i in range(150)]
    stdin = f"{len(names)}\n" + "\n".join(names) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
