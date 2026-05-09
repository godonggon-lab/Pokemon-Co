from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    idx = 1
    out = []
    for _ in range(nums[0]):
        n = nums[idx]
        pre = nums[idx + 1:idx + 1 + n]
        ino = nums[idx + 1 + n:idx + 1 + 2 * n]
        idx += 1 + 2 * n

        def post(preorder: list[int], inorder: list[int]) -> list[int]:
            if not preorder:
                return []
            root = preorder[0]
            mid = inorder.index(root)
            return post(preorder[1:1 + mid], inorder[:mid]) + post(preorder[1 + mid:], inorder[mid + 1:]) + [root]

        out.append(" ".join(map(str, post(pre, ino))))
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n1\n1\n1\n",
        "1\n3\n1 2 3\n2 1 3\n",
        "1\n3\n1 2 3\n1 2 3\n",
        "2\n3\n1 2 3\n2 1 3\n4\n1 2 4 3\n4 2 1 3\n",
        "1\n5\n1 2 4 5 3\n4 2 5 1 3\n",
        "2\n1\n7\n7\n5\n1 2 3 4 5\n3 2 4 1 5\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
