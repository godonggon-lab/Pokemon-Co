from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    it = iter(map(int, stdin.split()))
    t = next(it)
    out: list[str] = []
    for _ in range(t):
        candies = next(it)
        box_count = next(it)
        boxes = [next(it) * next(it) for _ in range(box_count)]
        boxes.sort(reverse=True)
        total = 0
        used = 0
        for size in boxes:
            total += size
            used += 1
            if total >= candies:
                break
        out.append(str(used))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n1 1\n1 1\n",
        "1\n10 3\n1 1\n2 2\n3 3\n",
        "1\n10 3\n2 3\n2 2\n1 1\n",
        "2\n20 4\n1 10\n2 3\n4 4\n1 1\n5 2\n1 2\n2 2\n",
        "1\n100 5\n10 1\n5 5\n3 9\n1 100\n2 7\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]

    boxes = "\n".join(f"{i % 10 + 1} {i % 7 + 1}" for i in range(100))
    stdin = f"1\n2000 100\n{boxes}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
