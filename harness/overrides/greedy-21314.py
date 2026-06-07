from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('M\n', '1\r\n1\r\n'),
        edge('MKM\n', '501\r\n151\r\n'),
        stress('MMKMMMKMMMM\n', '50050001111\r\n10510051000\r\n'),
    ]
