from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 1\n3 1 2 3\n', ''),
        edge('3 2\n2 1 2\n2 2 1\n', ''),
        edge('1 0\n', ''),
        edge('4 1\n4 1 2 3 4\n', ''),
        edge('4 2\n2 1 3\n2 2 4\n', ''),
        stress('5 3\n3 1 3 5\n2 2 4\n3 1 2 4\n', ''),
    ]

def check_output(stdin: str, expected: str, actual: str) -> bool:
    try:
        data = list(map(int, stdin.split()))
    except ValueError:
        return False
    if len(data) < 2:
        return False
    n, m = data[0], data[1]
    constraints = []
    idx = 2
    for _ in range(m):
        if idx >= len(data):
            return False
        k = data[idx]
        idx += 1
        seq = data[idx:idx + k]
        idx += k
        if len(seq) != k:
            return False
        constraints.extend(zip(seq, seq[1:]))

    def has_cycle() -> bool:
        graph = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)
        for a, b in constraints:
            graph[a].append(b)
            indeg[b] += 1
        queue = [i for i in range(1, n + 1) if indeg[i] == 0]
        head = 0
        seen = 0
        while head < len(queue):
            x = queue[head]
            head += 1
            seen += 1
            for nx in graph[x]:
                indeg[nx] -= 1
                if indeg[nx] == 0:
                    queue.append(nx)
        return seen != n

    if has_cycle():
        return actual.strip() == "0"
    try:
        tokens = list(map(int, actual.split()))
    except ValueError:
        return False
    if len(tokens) != n or set(tokens) != set(range(1, n + 1)):
        return False
    pos = {value: idx for idx, value in enumerate(tokens)}
    return all(pos[a] < pos[b] for a, b in constraints)
