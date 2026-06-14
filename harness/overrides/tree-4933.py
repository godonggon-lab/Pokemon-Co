from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2\nnil nil A\nnil nil A\nnil nil A nil B\nnil nil B nil A\n', 'true\r\nfalse\r\n'),
        edge('1\nnil nil A nil B\nnil nil A nil C\n', 'false\r\n'),
        edge('1\nnil nil A\nnil nil A\n', 'true\r\n'),
        edge('1\nnil nil A\nnil nil B\n', 'false\r\n'),
        edge('1\nnil nil A nil B\nnil nil B nil A\n', 'false\r\n'),
        stress('2\nnil nil A nil B nil C\nnil nil C nil B nil A\nnil nil X\nnil nil Y\n', 'false\r\nfalse\r\n'),
    ]
