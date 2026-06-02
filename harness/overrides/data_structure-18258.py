from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    queue = deque()
    out = []
    for command in lines[1:1 + n]:
        if command.startswith("push"):
            queue.append(command.split()[1])
        elif command == "pop":
            out.append(queue.popleft() if queue else "-1")
        elif command == "size":
            out.append(str(len(queue)))
        elif command == "empty":
            out.append("0" if queue else "1")
        elif command == "front":
            out.append(queue[0] if queue else "-1")
        elif command == "back":
            out.append(queue[-1] if queue else "-1")
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\nempty\n"),
        edge("3\npush 1\nfront\nback\n"),
        edge("5\npop\npush 10\npop\npop\nsize\n"),
        edge(
            "15\n"
            "push 1\npush 2\nfront\nback\nsize\nempty\n"
            "pop\npop\npop\nsize\nempty\npush 3\nempty\nfront\nback\n"
        ),
        edge(
            "12\n"
            "push -1\npush 0\npush 7\nfront\nback\npop\nfront\n"
            "size\npop\npop\npop\nempty\n"
        ),
        stress(
            "60\n"
            + "\n".join(
                [f"push {i}" for i in range(1, 21)]
                + ["front", "back", "size"]
                + ["pop" for _ in range(20)]
                + ["empty", "pop"]
                + [f"push {i}" for i in range(21, 35)]
                + ["size"]
            )
            + "\n"
        ),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
