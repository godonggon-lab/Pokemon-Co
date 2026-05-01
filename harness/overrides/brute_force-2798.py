"""
2798 블랙잭 — 카드 개수 N, 합 한도 M, N개의 정수.
완전탐색 카테고리 일반 템플릿(_arr_NM)으로 충분히 커버되지만
명시적 override 예시로 둔다.
"""
from __future__ import annotations
import random
from typing import List


def gen_inputs(_seed: int) -> List[str]:
    cases: List[str] = []
    # 고정된 엣지/일반 케이스 + 결정적 랜덤 케이스
    cases.append("5 21\n5 6 7 8 9\n")          # 정확히 21
    cases.append("10 500\n93 181 245 214 315 36 185 138 216 295\n")
    cases.append("3 5\n1 2 3\n")                # 합=6 > 5 → 6은 안되고 1+2+3은 X
    for i in range(3):
        rng = random.Random(f"2798:{i}")
        n = rng.randint(3, 12)
        m = rng.randint(20, 300)
        arr = [rng.randint(1, 100) for _ in range(n)]
        cases.append(f"{n} {m}\n" + " ".join(map(str, arr)) + "\n")
    return cases
