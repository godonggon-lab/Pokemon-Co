from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('A\nA\n', '1\r\n'),
        edge('A\nB\n', '0\r\n'),
        edge('ABCBDAB\nBDCABA\n', '4\r\n'),
        edge('AAAA\nBBBB\n', '0\r\n'),
        edge('XMJYAUZ\nMZJAWXU\n', '4\r\n'),
        stress('ABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCDABCD\nACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBDACBD\n', '75\r\n'),
    ]
