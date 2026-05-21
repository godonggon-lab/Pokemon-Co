from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _to_sec(value: str) -> int:
    h, m, s = map(int, value.split(":"))
    return h * 3600 + m * 60 + s


def _good(sec: int) -> bool:
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return (h * 10000 + m * 100 + s) % 3 == 0


def _solve(stdin: str) -> str:
    out: list[str] = []
    for line in stdin.strip().splitlines():
        start_s, end_s = line.split()
        start = _to_sec(start_s)
        end = _to_sec(end_s)
        if start <= end:
            seconds = range(start, end + 1)
        else:
            seconds = list(range(start, 24 * 3600)) + list(range(0, end + 1))
        out.append(str(sum(1 for sec in seconds if _good(sec))))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "00:00:00 00:00:00\n00:00:01 00:00:02\n23:59:58 00:00:02\n",
        "00:00:00 23:59:59\n12:00:00 12:34:56\n23:00:00 01:00:00\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("00:00:00 23:59:59\n00:00:01 00:00:00\n11:11:11 22:22:22\n", _solve("00:00:00 23:59:59\n00:00:01 00:00:00\n11:11:11 22:22:22\n")))
    return cases
