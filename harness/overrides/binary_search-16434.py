from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, initial_attack = map(int, lines[0].split())
    rooms = [tuple(map(int, line.split())) for line in lines[1:]]

    def survive(max_hp: int) -> bool:
        hp = max_hp
        attack = initial_attack
        for room_type, value, health in rooms:
            if room_type == 1:
                hits = (health + attack - 1) // attack
                hp -= value * (hits - 1)
                if hp <= 0:
                    return False
            else:
                attack += value
                hp = min(max_hp, hp + health)
        return True

    low, high = 1, 10**18
    while low < high:
        mid = (low + high) // 2
        if survive(mid):
            high = mid
        else:
            low = mid + 1
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 10\n1 1 10\n"),
        edge("1 1\n1 10 1\n"),
        edge("2 3\n1 10 10\n2 10 10\n"),
        edge("3 2\n2 5 10\n1 4 8\n1 1 10\n"),
        edge("4 1\n1 1 3\n2 10 10\n1 20 20\n2 1 100\n"),
        stress("4 5\n1 7 20\n2 3 10\n1 20 30\n1 1 100\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
