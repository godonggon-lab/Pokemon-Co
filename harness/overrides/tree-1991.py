from harness.cases import edge


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    tree: dict[str, tuple[str, str]] = {}
    for line in lines[1 : n + 1]:
        root, left, right = line.split()
        tree[root] = (left, right)

    def preorder(node: str) -> str:
        if node == ".":
            return ""
        left, right = tree[node]
        return node + preorder(left) + preorder(right)

    def inorder(node: str) -> str:
        if node == ".":
            return ""
        left, right = tree[node]
        return inorder(left) + node + inorder(right)

    def postorder(node: str) -> str:
        if node == ".":
            return ""
        left, right = tree[node]
        return postorder(left) + postorder(right) + node

    return "\n".join([preorder("A"), inorder("A"), postorder("A")]) + "\n"


def gen_inputs(_seed):
    cases = [
        "1\nA . .\n",
        "3\nA B C\nB . .\nC . .\n",
        "5\nA B C\nB D .\nC . E\nD . .\nE . .\n",
        "7\nA B C\nB D E\nC F G\nD . .\nE . .\nF . .\nG . .\n",
    ]
    return [edge(case, _solve(case)) for case in cases]
