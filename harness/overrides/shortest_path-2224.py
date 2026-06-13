from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\nA => B\n', '1\r\nA => B\r\n'),
        edge('3\nA => B\nB => C\na => A\n', '6\r\nA => B\r\nA => C\r\nB => C\r\na => A\r\na => B\r\na => C\r\n'),
        edge('1\nA => A\n', '0\r\n'),
        edge('2\nA => B\nB => A\n', '2\r\nA => B\r\nB => A\r\n'),
        edge('3\nZ => a\na => z\nZ => z\n', '3\r\nZ => a\r\nZ => z\r\na => z\r\n'),
        stress('5\nA => B\nB => C\nC => D\na => b\nb => C\n', '11\r\nA => B\r\nA => C\r\nA => D\r\nB => C\r\nB => D\r\nC => D\r\na => C\r\na => D\r\na => b\r\nb => C\r\nb => D\r\n'),
    ]
