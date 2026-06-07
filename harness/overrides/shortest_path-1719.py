from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n1 2 5\n', '- 2\r\n1 -\r\n'),
        edge('3 2\n1 2 1\n2 3 1\n', '- 2 2\r\n1 - 3\r\n2 2 -\r\n'),
        edge('3 3\n1 2 5\n1 3 2\n2 3 1\n', '- 3 3\r\n3 - 3\r\n1 2 -\r\n'),
        edge('4 3\n1 2 1\n1 3 1\n1 4 1\n', '- 2 3 4\r\n1 - 1 1\r\n1 1 - 1\r\n1 1 1 -\r\n'),
        edge('4 4\n1 2 3\n2 3 4\n3 4 5\n1 4 20\n', '- 2 2 2\r\n1 - 3 3\r\n2 2 - 4\r\n3 3 3 -\r\n'),
        stress('6 7\n1 2 2\n1 3 5\n2 3 1\n2 4 2\n3 5 2\n4 6 3\n5 6 1\n', '- 2 2 2 2 2\r\n1 - 3 4 3 3\r\n2 2 - 2 5 5\r\n2 2 2 - 6 6\r\n3 3 3 6 - 6\r\n5 5 5 4 5 -\r\n'),
    ]
