from __future__ import annotations
from itertools import permutations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 1\n1 2 3 4\n1 2 3 4\n1 2\n1 2\n1 2 1\n"),
        edge("1 0\n1 1 1 1\n1 1\n"),
        edge("2 1\n1 1 1 1\n2 2 2 2\n1 1\n2 2\n1 2 1\n"),
        edge("2 0\n1 2 3 4\n4 3 2 1\n1 2\n1 2\n"),
        edge("3 1\n1 1 1 1\n1 2 1 2\n2 2 2 2\n1 2\n2 3\n1 3\n1 2 2\n"),
        stress("3 2\n1 2 3 4\n1 2 3 4\n4 3 2 1\n1 2\n2 3\n1 3\n1 2 2\n2 3 3\n"),
    ]
    return [{**case, "expected": ""} for case in cases]

def check_output(stdin: str, expected: str, actual: str) -> bool:
    n, frogs, prefers, logs = _parse(stdin)
    expected_yes = _exists(n, frogs, prefers, logs)
    lines = [line.strip() for line in actual.strip().splitlines() if line.strip()]
    if not lines:
        return False
    if lines[0] == "NO":
        return not expected_yes
    if lines[0] != "YES" or not expected_yes or len(lines) < 2:
        return False
    try:
        arr = list(map(int, lines[1].split()))
    except ValueError:
        return False
    if len(arr) != n or sorted(arr) != list(range(1, n + 1)):
        return False
    for lotus, frog in enumerate(arr, 1):
        if lotus not in prefers[frog]:
            return False
    for a, b, t in logs:
        if frogs[arr[a - 1]][t - 1] != frogs[arr[b - 1]][t - 1]:
            return False
    return True

def _parse(stdin: str):
    it = iter(map(int, stdin.split()))
    n = next(it); m = next(it)
    frogs = [()] + [tuple(next(it) for _ in range(4)) for _ in range(n)]
    prefers = [set()]
    for _ in range(n):
        prefers.append({next(it), next(it)})
    logs = [(next(it), next(it), next(it)) for _ in range(m)]
    return n, frogs, prefers, logs

def _exists(n, frogs, prefers, logs) -> bool:
    for arr in permutations(range(1, n + 1)):
        if all(i + 1 in prefers[frog] for i, frog in enumerate(arr)):
            if all(frogs[arr[a - 1]][t - 1] == frogs[arr[b - 1]][t - 1] for a, b, t in logs):
                return True
    return False
