from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("00000000\n11111111\n22222222\n33333333\n44444444\n55555555\n66666666\n"),
        edge("00112233\n44556600\n11223344\n55660011\n22334455\n66001122\n33445566\n"),
        stress("01234567\n12345670\n23456701\n34567012\n45670123\n56701234\n67012345\n"),
    ]
