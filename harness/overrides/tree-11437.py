from collections import deque

from harness.cases import edge


def _solve(stdin: str) -> str:
    it = iter(stdin.strip().split())
    n = int(next(it))
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(next(it))
        b = int(next(it))
        graph[a].append(b)
        graph[b].append(a)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    q = deque([1])
    parent[1] = 1
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if parent[nxt]:
                continue
            parent[nxt] = cur
            depth[nxt] = depth[cur] + 1
            q.append(nxt)

    def lca(a: int, b: int) -> int:
        while depth[a] > depth[b]:
            a = parent[a]
        while depth[b] > depth[a]:
            b = parent[b]
        while a != b:
            a = parent[a]
            b = parent[b]
        return a

    m = int(next(it))
    out = []
    for _ in range(m):
        out.append(str(lca(int(next(it)), int(next(it)))))
    return "\n".join(out) + "\n"


def gen_inputs(_seed):
    cases = [
        "2\n1 2\n3\n1 2\n2 1\n1 1\n",
        "7\n1 2\n1 3\n2 4\n2 5\n3 6\n6 7\n5\n4 5\n4 7\n6 7\n2 7\n1 7\n",
        "8\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n7 8\n4\n8 5\n7 3\n2 8\n1 8\n",
        "9\n1 2\n1 3\n1 4\n4 5\n4 6\n6 7\n6 8\n8 9\n5\n5 7\n7 9\n2 3\n8 9\n4 9\n",
    ]
    return [edge(case, _solve(case)) for case in cases]
