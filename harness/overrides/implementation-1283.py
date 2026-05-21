from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def _solve(stdin: str) -> str:
    lines = stdin.splitlines()
    n = int(lines[0])
    used: set[str] = set()
    out: list[str] = []
    for line in lines[1 : 1 + n]:
        words = line.split(" ")
        picked = None
        offset = 0
        for word in words:
            if word and word[0].lower() not in used:
                picked = offset
                used.add(word[0].lower())
                break
            offset += len(word) + 1
        if picked is None:
            for idx, ch in enumerate(line):
                if ch != " " and ch.lower() not in used:
                    picked = idx
                    used.add(ch.lower())
                    break
        out.append(line if picked is None else line[:picked] + "[" + line[picked] + "]" + line[picked + 1 :])
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "5\nNew\nOpen\nSave\nSave As\nSave All\n",
        "4\nAdd Folder\nApple Pie\nopen file\ncopy paste\n",
        "3\na b c\nA B C\nzzz\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
