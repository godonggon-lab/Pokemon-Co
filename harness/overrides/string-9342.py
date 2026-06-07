from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\nAFC\n', 'Infected!\r\n'),
        edge('2\nAAFFCC\nBAFCC\n', 'Infected!\r\nInfected!\r\n'),
        edge('3\nAFC\nAFFCC\nAAFCCB\n', 'Infected!\r\nInfected!\r\nInfected!\r\n'),
        edge('4\nXYZ\nAAFC\nAAFCCC\nFAFC\n', 'Good\r\nInfected!\r\nInfected!\r\nInfected!\r\n'),
        edge('5\nAFFFFCC\nCAAFFCC\nAAFFFCCC\nBAAAFFFC\nAAAFCCCD\n', 'Infected!\r\nInfected!\r\nInfected!\r\nInfected!\r\nInfected!\r\n'),
        stress('6\nAFC\nBAFC\nAFFFCCCC\nDAFC\nEAAFFCCF\nGAFCC\n', 'Infected!\r\nInfected!\r\nInfected!\r\nInfected!\r\nInfected!\r\nGood\r\n'),
    ]
