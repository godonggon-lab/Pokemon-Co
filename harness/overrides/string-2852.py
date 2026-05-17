from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


TOTAL = 48 * 60


def _to_sec(value: str) -> int:
    minute, second = map(int, value.split(":"))
    return minute * 60 + second


def _fmt(sec: int) -> str:
    return f"{sec // 60:02d}:{sec % 60:02d}"


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    score = [0, 0]
    lead_time = [0, 0]
    last = 0
    for line in lines[1 : 1 + n]:
        team_s, time_s = line.split()
        now = _to_sec(time_s)
        if score[0] > score[1]:
            lead_time[0] += now - last
        elif score[1] > score[0]:
            lead_time[1] += now - last
        score[int(team_s) - 1] += 1
        last = now
    if score[0] > score[1]:
        lead_time[0] += TOTAL - last
    elif score[1] > score[0]:
        lead_time[1] += TOTAL - last
    return f"{_fmt(lead_time[0])}\n{_fmt(lead_time[1])}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n1 20:00\n",
        "2\n1 01:00\n2 02:00\n",
        "5\n1 01:00\n1 02:00\n2 03:00\n2 04:00\n1 47:59\n",
        "4\n2 00:00\n1 10:00\n1 20:00\n2 30:00\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    events = [f"{1 + (i % 2)} {i // 60:02d}:{i % 60:02d}" for i in range(0, 1200, 17)]
    stdin = f"{len(events)}\n" + "\n".join(events) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
