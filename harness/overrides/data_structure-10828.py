from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    stack = []
    out = []
    for command in lines[1:1 + n]:
        if command.startswith("push"):
            stack.append(command.split()[1])
        elif command == "pop":
            out.append(stack.pop() if stack else "-1")
        elif command == "size":
            out.append(str(len(stack)))
        elif command == "empty":
            out.append("0" if stack else "1")
        elif command == "top":
            out.append(stack[-1] if stack else "-1")
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\nempty\n"),
        edge("3\npush 1\ntop\npop\n"),
        edge("5\npop\npush 2\npush 3\nsize\ntop\n"),
        edge("6\npush 1\npush 2\npop\npop\npop\nempty\n"),
        edge("4\npush 9\nsize\ntop\nempty\n"),
        stress("10\npush 1\npush 2\npush 3\npop\ntop\nsize\npop\npop\npop\nempty\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
