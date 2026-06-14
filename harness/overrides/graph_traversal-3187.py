from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\nk\n', '1 0\r\n'),
        edge('3 3\n...\n.kv\n...\n', '0 1\r\n'),
        edge('4 5\n####.\n#kv#.\n#kk#v\n.....\n', '3 0\r\n'),
        edge('1 3\nkvk\n', '2 0\r\n'),
        edge('3 5\n#####\n#kvv#\n#####\n', '0 2\r\n'),
        stress('10 10\n..#kv#....\nkv.kv.kv.k\n..#kv#....\nkv.kv.kv.k\n..#kv#....\nkv.kv.kv.k\n..#kv#....\nkv.kv.kv.k\n..#kv#....\nkv.kv.kv.k\n', '25 0\r\n'),
    ]
