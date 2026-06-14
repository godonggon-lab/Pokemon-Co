from __future__ import annotations

from collections import defaultdict
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    children: dict[str, list[tuple[str, bool]]] = defaultdict(list)
    for line in lines[1 : 1 + n + m]:
        parent, child, is_folder = line.split()
        children[parent].append((child, is_folder == "1"))

    def collect(folder: str) -> tuple[int, int]:
        names: set[str] = set()
        total = 0
        stack = [folder]
        while stack:
            cur = stack.pop()
            for name, is_folder in children[cur]:
                if is_folder:
                    stack.append(name)
                else:
                    names.add(name)
                    total += 1
        return len(names), total

    q_idx = 1 + n + m
    q = int(lines[q_idx])
    out: list[str] = []
    for line in lines[q_idx + 1 : q_idx + 1 + q]:
        out.append("%d %d" % collect(line.split("/")[-1]))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2 3\nmain FolderA 1\nFolderA file1 0\nmain file2 0\nFolderA file1 0\nFolderA file3 0\n2\nmain\nmain/FolderA\n",
        "1 2\nmain docs 1\ndocs a 0\ndocs b 0\n1\nmain/docs\n",
        "0 2\nmain a 0\nmain a 0\n1\nmain\n",
        "0 1\nmain only 0\n1\nmain\n",
        "2 2\nmain a 1\na b 1\nb x 0\nb x 0\n3\nmain\nmain/a\nmain/a/b\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    lines = [
        "4 6",
        "main a 1",
        "main b 1",
        "a c 1",
        "b d 1",
        "a x 0",
        "a y 0",
        "c x 0",
        "b z 0",
        "d z 0",
        "d w 0",
        "4",
        "main",
        "main/a",
        "main/a/c",
        "main/b/d",
    ]
    hard = "\n".join(lines) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
