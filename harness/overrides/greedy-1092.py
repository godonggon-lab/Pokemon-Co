from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n = nums[0]; cranes = sorted(nums[1:1 + n], reverse=True)
    m_idx = 1 + n; boxes = sorted(nums[m_idx + 1:], reverse=True)
    if boxes and boxes[0] > cranes[0]:
        return "-1\n"
    time = 0
    while boxes:
        time += 1
        used = []
        for crane in cranes:
            for i, box in enumerate(boxes):
                if i not in used and box <= crane:
                    used.append(i)
                    break
        for i in sorted(used, reverse=True):
            boxes.pop(i)
    return f"{time}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n10\n1\n5\n", "1\n5\n1\n10\n", "2\n10 5\n3\n7 5 3\n", "3\n6 8 9\n5\n2 5 2 4 7\n", "3\n1 2 3\n6\n1 1 1 2 2 3\n", "4\n10 9 8 7\n10\n1 2 3 4 5 6 7 8 9 10\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
