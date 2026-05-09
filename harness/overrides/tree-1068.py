from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n = nums[0]
    parents = nums[1:1 + n]
    delete = nums[1 + n]
    children = [[] for _ in range(n)]
    root = -1
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            children[parent].append(i)
    if delete == root:
        return "0\n"
    for arr in children:
        if delete in arr:
            arr.remove(delete)

    def dfs(node: int) -> int:
        return 1 if not children[node] else sum(dfs(child) for child in children[node])

    return f"{dfs(root)}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n-1\n0\n", "2\n-1 0\n1\n", "3\n-1 0 0\n1\n", "5\n-1 0 0 1 1\n1\n", "5\n-1 0 0 1 1\n2\n", "7\n-1 0 0 1 1 2 2\n0\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
