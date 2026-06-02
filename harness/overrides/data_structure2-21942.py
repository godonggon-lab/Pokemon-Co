from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


MONTH_DAYS = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]


def _minute(line: str) -> tuple[str, str, int]:
    date, time, item, person = line.split()
    _year, month, day = map(int, date.split("-"))
    hour, minute = map(int, time.split(":"))
    total = (MONTH_DAYS[month - 1] + day) * 24 * 60 + hour * 60 + minute
    return person, item, total


def _solve(data: str) -> str:
    lines = data.splitlines()
    n_text, limit_text, fee_text = lines[0].split()
    n, fee = int(n_text), int(fee_text)
    days, time = limit_text.split("/")
    hours, minutes = map(int, time.split(":"))
    limit = int(days) * 24 * 60 + hours * 60 + minutes
    rented: dict[str, dict[str, int]] = {}
    fines: dict[str, int] = {}
    for line in lines[1:1 + n]:
        person, item, current = _minute(line)
        rented.setdefault(person, {})
        if item in rented[person]:
            elapsed = current - rented[person].pop(item)
            if elapsed > limit:
                fines[person] = fines.get(person, 0) + (elapsed - limit) * fee
        else:
            rented[person][item] = current
    if not fines:
        return "-1"
    return "\n".join(f"{person} {fines[person]}" for person in sorted(fines))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 001/00:01 10\n2021-01-01 00:00 part alice\n"),
        edge("2 001/00:01 10\n2021-01-01 00:00 part alice\n2021-01-01 00:01 part alice\n"),
        edge("2 000/00:01 100\n2021-01-01 00:00 lens bob\n2021-01-01 00:03 lens bob\n"),
        edge("4 001/00:00 5\n2021-01-01 00:00 a kim\n2021-01-01 00:30 a kim\n2021-01-01 01:00 b lee\n2021-01-03 01:01 b lee\n"),
        edge("5 000/00:10 2\n2021-01-01 00:00 p a\n2021-01-01 00:20 p a\n2021-01-01 00:00 q b\n2021-01-01 00:09 q b\n2021-01-02 00:00 r c\n"),
        stress("6 001/12:00 3\n2021-01-01 00:00 x aa\n2021-01-02 13:00 x aa\n2021-01-01 00:00 y bb\n2021-01-01 12:00 y bb\n2021-01-03 00:00 z cc\n2021-01-05 00:01 z cc\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
