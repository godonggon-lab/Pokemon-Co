from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    dna = lines[1:1 + n]
    answer = []
    distance = 0
    for col in range(m):
        counts = {base: 0 for base in "ACGT"}
        for row in dna:
            counts[row[col]] += 1
        base = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[0]
        answer.append(base[0])
        distance += n - base[1]
    return "".join(answer) + "\n" + str(distance)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\nA\n"),
        edge("2 4\nAAAA\nTTTT\n"),
        edge("3 5\nAAAAA\nAACAA\nAAGAA\n"),
        edge("4 6\nTATATA\nTATATA\nCCCCCC\nGGGGGG\n"),
        edge("5 8\nACGTACGT\nACGTTCGT\nACGTACGA\nTCGTACGT\nACGTACGT\n"),
        stress("6 10\nAAAAAAAAAA\nCCCCCCCCCC\nGGGGGGGGGG\nTTTTTTTTTT\nACGTACGTAC\nTGCATGCATG\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
