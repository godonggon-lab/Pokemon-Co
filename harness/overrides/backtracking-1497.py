from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, _m = map(int, lines[0].split())
    masks: list[int] = []
    for line in lines[1 : 1 + n]:
        _name, songs = line.split()
        mask = 0
        for idx, ch in enumerate(songs):
            if ch == "Y":
                mask |= 1 << idx
        masks.append(mask)
    best_songs = 0
    best_count = 10**9
    for bits in range(1, 1 << n):
        mask = 0
        count = 0
        for idx in range(n):
            if bits & (1 << idx):
                mask |= masks[idx]
                count += 1
        songs = mask.bit_count()
        if songs > best_songs or (songs == best_songs and count < best_count):
            best_songs = songs
            best_count = count
    return str(-1 if best_songs == 0 else best_count)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3 5\ng1 YNNYY\ng2 NYNYN\ng3 NNNNN\n",
        "2 3\na NNN\nb NNN\n",
        "1 4\nsolo YYYY\n",
        "4 4\na YYNN\nb NNYY\nc YNYN\nd NYNY\n",
        "3 4\na YNNN\nb NYNN\nc NNYN\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    rows = []
    for i in range(10):
        songs = "".join("Y" if (i + j) % 3 != 0 else "N" for j in range(12))
        rows.append(f"g{i} {songs}")
    hard = "10 12\n" + "\n".join(rows) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
