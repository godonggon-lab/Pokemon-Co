from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    t = int(lines[0])
    index = 1
    out = []
    for _ in range(t):
        stats = [list(map(int, lines[index + row].split())) for row in range(11)]
        index += 11
        used = [False] * 11
        best = 0

        def dfs(player: int, total: int) -> None:
            nonlocal best
            if player == 11:
                best = max(best, total)
                return
            for position in range(11):
                if not used[position] and stats[player][position] > 0:
                    used[position] = True
                    dfs(player + 1, total + stats[player][position])
                    used[position] = False

        dfs(0, 0)
        out.append(str(best))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    ident = "\n".join(" ".join("10" if i == j else "0" for j in range(11)) for i in range(11))
    shifted = "\n".join(" ".join("9" if j == (i + 1) % 11 else ("5" if j == i else "0") for j in range(11)) for i in range(11))
    paired = "\n".join(" ".join("8" if j in {i, (i + 1) % 11} else "0" for j in range(11)) for i in range(11))
    descending = "\n".join(" ".join(str(11 - j) if j >= i else "0" for j in range(11)) for i in range(11))
    sparse = "\n".join(" ".join("7" if j in {i, (i + 2) % 11} else "0" for j in range(11)) for i in range(11))
    cases = [
        edge("1\n" + ident + "\n"),
        edge("1\n" + paired + "\n"),
        edge("1\n" + descending + "\n"),
        edge("1\n" + sparse + "\n"),
        edge("2\n" + ident + "\n" + shifted + "\n"),
        stress("1\n" + shifted + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
