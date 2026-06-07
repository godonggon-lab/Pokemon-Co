from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('END\n', ''),
        edge('abc\nEND\n', 'cba\r\n'),
        edge('hello world\nEND\n', 'dlrow olleh\r\n'),
        edge('madam\nracecar\nEND\n', 'madam\r\nracecar\r\n'),
        edge('12345\n!@# $\nEND\n', '54321\r\n$ #@!\r\n'),
        stress('DongJun CodeDex\nboj override\nEND\n', 'xeDedoC nuJgnoD\r\nedirrevo job\r\n'),
    ]
