from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nabc\n", "abc\n"),
        edge("1\nabc<d\n", "abdc\n"),
        edge("1\nabc<<d\n", "adbc\n"),
        edge("1\nabc<-d\n", "adc\n"),
        edge("2\n<<BP<A>>Cd-\nThIsIsS3Cr3t\n", "BAPC\nThIsIsS3Cr3t\n"),
        stress("1\na<b<c<d>e-f\n", "dcfba\n"),
    ]
