from harness.cases import edge, stress


def _lca(parent: list[int], a: int, b: int) -> int:
    seen = set()
    while a:
        seen.add(a)
        a = parent[a]
    while b not in seen:
        b = parent[b]
    return b


def _solve(stdin: str) -> str:
    it = iter(stdin.strip().split())
    t = int(next(it))
    out: list[str] = []
    for _ in range(t):
        n = int(next(it))
        parent = [0] * (n + 1)
        for _ in range(n - 1):
            p = int(next(it))
            c = int(next(it))
            parent[c] = p
        a = int(next(it))
        b = int(next(it))
        out.append(str(_lca(parent, a, b)))
    return "\n".join(out) + "\n"


def gen_inputs(_seed):
    cases = [
        "1\n2\n1 2\n1 2\n",
        "1\n5\n1 2\n1 3\n3 4\n3 5\n4 5\n",
        "2\n7\n1 2\n1 3\n2 4\n2 5\n3 6\n6 7\n4 5\n5\n2 1\n2 3\n3 4\n3 5\n1 5\n",
        "1\n8\n4 2\n4 6\n2 1\n2 3\n6 5\n6 7\n7 8\n1 8\n",
    ]
    out = [edge(case, _solve(case)) for case in cases]
    extra = "1\n10\n1 2\n1 3\n2 4\n2 5\n5 6\n5 7\n3 8\n8 9\n8 10\n6 7\n"
    multi = "3\n4\n1 2\n2 3\n3 4\n2 4\n6\n1 2\n1 3\n3 4\n3 5\n5 6\n4 6\n7\n4 2\n4 6\n2 1\n2 3\n6 5\n6 7\n1 7\n"
    out.append(edge(extra, _solve(extra)))
    out.append(stress(multi, _solve(multi)))
    return out
