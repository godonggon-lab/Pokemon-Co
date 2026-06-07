from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('5 6\n......\n..xx..\n..xx..\n..xx..\nxxxxxx\n1\n3\n', '......\r\n..xx..\r\n...x..\r\n..xx..\r\nxxxxxx\r\n'),
        edge('6 7\n.......\n..xxx..\n..x.x..\n..xxx..\n...x...\nxxxxxxx\n2\n2 4\n', '.......\r\n.......\r\n..xx...\r\n..x.x..\r\n..xxx..\r\nxxxxxxx\r\n'),
        stress('7 8\n........\n...xx...\n..xxxx..\n...xx...\n..xxxx..\n...xx...\nxxxxxxxx\n3\n2 5 3\n', '........\r\n...xx...\r\n..xxx...\r\n...xx...\r\n...xxx..\r\n....x...\r\nxxxxxxxx\r\n'),
    ]
