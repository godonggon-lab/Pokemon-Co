from __future__ import annotations
from collections import deque
from typing import List
from harness.cases import GeneratedCase, edge, stress

MASKS = []
for i in range(3):
    for j in range(3):
        mask = 0
        for x, y in ((i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < 3 and 0 <= y < 3:
                mask ^= 1 << (x * 3 + y)
        MASKS.append(mask)

DIST = [-1] * 512
DIST[0] = 0
queue = deque([0])
while queue:
    state = queue.popleft()
    for mask in MASKS:
        next_state = state ^ mask
        if DIST[next_state] == -1:
            DIST[next_state] = DIST[state] + 1
            queue.append(next_state)

def _solve(data: str) -> str:
    lines = data.splitlines()
    index = 1
    out = []
    for _ in range(int(lines[0])):
        state = 0
        for i in range(3):
            row = lines[index + i]
            for j, char in enumerate(row):
                if char == "*":
                    state |= 1 << (i * 3 + j)
        index += 3
        out.append(str(DIST[state]))
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n...\n...\n...\n"),
        edge("1\n*..\n...\n...\n"),
        edge("1\n.*.\n***\n.*.\n"),
        edge("2\n***\n***\n***\n*..\n.*.\n..*\n"),
        edge("2\n...\n***\n...\n***\n...\n***\n"),
        stress("3\n*.*\n.*.\n*.*\n***\n...\n***\n..*\n*..\n.*.\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
