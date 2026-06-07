from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('word\n', '1\r\n'),
        edge(' hello world \n', '2\r\n'),
        edge('   \n', '0\r\n'),
        edge('a b c d e\n', '5\r\n'),
        edge('  multiple   spaces  inside  \n', '3\r\n'),
        stress('The Curious Case Of DongJun CodeDex\n', '6\r\n'),
    ]
