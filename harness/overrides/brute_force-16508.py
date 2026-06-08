from __future__ import annotations
from collections import Counter
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    target = Counter(lines[0].strip())
    n = int(lines[1])
    books = []
    for line in lines[2:2 + n]:
        price, title = line.split(maxsplit=1)
        books.append((int(price), Counter(title)))
    answer = 10**9
    for mask in range(1, 1 << n):
        cost = 0
        letters = Counter()
        for i, (price, book_letters) in enumerate(books):
            if mask & (1 << i):
                cost += price
                letters += book_letters
        if all(letters[ch] >= count for ch, count in target.items()):
            answer = min(answer, cost)
    return str(answer if answer < 10**9 else -1)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("A\n1\n10 A\n"),
        edge("ABC\n2\n10 AB\n5 C\n"),
        edge("ABC\n1\n3 AB\n"),
        edge("AA\n2\n5 A\n8 AA\n"),
        edge("BAEK\n3\n10 BAE\n5 K\n100 CODE\n"),
        stress("DOG\n4\n5 DO\n6 OG\n10 CAT\n3 G\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
