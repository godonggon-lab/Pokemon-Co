from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 0\n', ''),
        edge('3 2\n1 3\n2 3\n', ''),
        stress('5 4\n1 2\n1 3\n3 4\n2 5\n', ''),
    ]

def check_output(stdin: str, expected: str, actual: str) -> bool:
    try:
        tokens = list(map(int, actual.split()))
        data = list(map(int, stdin.split()))
    except ValueError:
        return False
    if len(data) < 2:
        return False
    n, m = data[0], data[1]
    if len(tokens) != n or set(tokens) != set(range(1, n + 1)):
        return False
    pos = {value: idx for idx, value in enumerate(tokens)}
    idx = 2
    for _ in range(m):
        if idx + 1 >= len(data):
            return False
        a, b = data[idx], data[idx + 1]
        idx += 2
        if pos[a] >= pos[b]:
            return False
    return True
