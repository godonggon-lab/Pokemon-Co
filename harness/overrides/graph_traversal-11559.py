from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('......\n......\n......\n......\n......\n......\n......\n......\n......\n......\n......\n......\n', '0\r\n'),
        edge('......\n......\n......\n......\n......\n......\n......\n......\n......\n......\n......\nRRRR..\n', '1\r\n'),
        stress('......\n......\n......\n......\n......\n......\n......\n......\nYYYY..\nYYYY..\nRRRR..\nRRRR..\n', '1\r\n'),
    ]
