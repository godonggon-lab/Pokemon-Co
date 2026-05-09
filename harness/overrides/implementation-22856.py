from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n = nums[0]
    left = [-1] * (n + 1)
    right = [-1] * (n + 1)
    edge_count = 0
    idx = 1
    for _ in range(n):
        node, lch, rch = nums[idx], nums[idx + 1], nums[idx + 2]
        idx += 3
        left[node], right[node] = lch, rch
        edge_count += (lch != -1) + (rch != -1)

    inorder = []

    def dfs(node: int) -> None:
        if node == -1:
            return
        dfs(left[node])
        inorder.append(node)
        dfs(right[node])

    dfs(1)
    end = inorder[-1]
    depth = 0
    cur = 1
    while cur != end:
        if end in subtree_nodes(left[cur], left, right):
            cur = left[cur]
        else:
            cur = right[cur]
        depth += 1
    return f"{edge_count * 2 - depth}\n"


def subtree_nodes(root: int, left: list[int], right: list[int]) -> set[int]:
    if root == -1:
        return set()
    return {root} | subtree_nodes(left[root], left, right) | subtree_nodes(right[root], left, right)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n1 -1 -1\n",
        "2\n1 2 -1\n2 -1 -1\n",
        "2\n1 -1 2\n2 -1 -1\n",
        "3\n1 2 3\n2 -1 -1\n3 -1 -1\n",
        "5\n1 2 3\n2 4 5\n3 -1 -1\n4 -1 -1\n5 -1 -1\n",
        "7\n1 2 3\n2 4 5\n3 6 7\n4 -1 -1\n5 -1 -1\n6 -1 -1\n7 -1 -1\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
