from __future__ import annotations

import bisect
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    problems: dict[int, tuple[int, int]] = {}
    by_group: dict[int, list[tuple[int, int]]] = {}
    all_items: list[tuple[int, int]] = []

    def add_item(p: int, level: int, group: int) -> None:
        problems[p] = (level, group)
        item = (level, p)
        by_group.setdefault(group, [])
        bisect.insort(by_group[group], item)
        bisect.insort(all_items, item)

    def remove_item(p: int) -> None:
        level, group = problems.pop(p)
        item = (level, p)
        by_group[group].pop(bisect.bisect_left(by_group[group], item))
        all_items.pop(bisect.bisect_left(all_items, item))

    for line in lines[1 : 1 + n]:
        p, level, group = map(int, line.split())
        add_item(p, level, group)
    m = int(lines[1 + n])
    out: list[str] = []
    for line in lines[2 + n : 2 + n + m]:
        parts = line.split()
        cmd = parts[0]
        if cmd == "add":
            add_item(int(parts[1]), int(parts[2]), int(parts[3]))
        elif cmd == "solved":
            remove_item(int(parts[1]))
        elif cmd == "recommend":
            group, x = int(parts[1]), int(parts[2])
            out.append(str(by_group[group][-1][1] if x == 1 else by_group[group][0][1]))
        elif cmd == "recommend2":
            x = int(parts[1])
            out.append(str(all_items[-1][1] if x == 1 else all_items[0][1]))
        else:
            x, level = int(parts[1]), int(parts[2])
            if x == 1:
                idx = bisect.bisect_left(all_items, (level, -1))
                out.append(str(all_items[idx][1] if idx < len(all_items) else -1))
            else:
                idx = bisect.bisect_left(all_items, (level, -1)) - 1
                out.append(str(all_items[idx][1] if idx >= 0 else -1))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "5\n1000 1 1\n1001 2 1\n19998 78 2\n2667 37 3\n2042 55 3\n8\nrecommend 1 1\nrecommend 1 -1\nrecommend2 1\nrecommend3 1 50\nrecommend3 -1 50\nsolved 1001\nadd 1001 100 1\nrecommend 1 1\n",
        "3\n1 10 1\n2 10 1\n3 20 2\n6\nrecommend2 -1\nrecommend2 1\nrecommend3 1 15\nrecommend3 -1 15\nsolved 3\nrecommend3 1 15\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    initial = [f"{1000 + i} {i % 100 + 1} {i % 7 + 1}" for i in range(1, 31)]
    commands = []
    for i in range(1, 21):
        commands.append("recommend2 1" if i % 2 else "recommend2 -1")
        commands.append(f"recommend3 1 {i * 3}")
    hard = f"{len(initial)}\n" + "\n".join(initial) + f"\n{len(commands)}\n" + "\n".join(commands) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
