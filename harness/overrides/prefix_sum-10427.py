from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    t = int(lines[0])
    answers: list[str] = []
    for line in lines[1 : 1 + t]:
        data = list(map(int, line.split()))
        n = data[0]
        arr = sorted(data[1:])
        prefix = [0]
        for value in arr:
            prefix.append(prefix[-1] + value)
        total = 0
        for size in range(1, n + 1):
            best = 10**30
            for end in range(size, n + 1):
                best = min(best, arr[end - 1] * size - (prefix[end] - prefix[end - size]))
            total += best
        answers.append(str(total))
    return "\n".join(answers)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n3 1 2 3\n",
        "2\n4 10 10 10 10\n5 1 3 6 10 15\n",
        "1\n6 8 1 4 9 2 7\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
