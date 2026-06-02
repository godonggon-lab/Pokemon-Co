from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    dq = deque()
    out = []
    for command in lines[1:1 + n]:
        if command.startswith("push_front"):
            dq.appendleft(command.split()[1])
        elif command.startswith("push_back"):
            dq.append(command.split()[1])
        elif command == "pop_front":
            out.append(dq.popleft() if dq else "-1")
        elif command == "pop_back":
            out.append(dq.pop() if dq else "-1")
        elif command == "size":
            out.append(str(len(dq)))
        elif command == "empty":
            out.append("0" if dq else "1")
        elif command == "front":
            out.append(dq[0] if dq else "-1")
        elif command == "back":
            out.append(dq[-1] if dq else "-1")
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\nempty\n"),
        edge("3\npush_front 1\nfront\nback\n"),
        edge("5\npush_back 1\npush_front 2\nfront\nback\nsize\n"),
        edge("6\npop_front\npush_back 1\npush_back 2\npop_back\npop_front\npop_front\n"),
        edge("6\npush_front 3\npush_back 4\npop_front\npop_back\nempty\nfront\n"),
        stress("10\npush_back 1\npush_front 2\npush_back 3\nfront\nback\npop_front\npop_back\nsize\npop_front\nempty\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
