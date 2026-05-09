from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nempty\n"),
        edge("3\npush 1\nfront\nback\n"),
        edge("5\npop\npush 10\npop\npop\nsize\n"),
        edge(
            "15\n"
            "push 1\npush 2\nfront\nback\nsize\nempty\n"
            "pop\npop\npop\nsize\nempty\npush 3\nempty\nfront\nback\n"
        ),
        edge(
            "12\n"
            "push -1\npush 0\npush 7\nfront\nback\npop\nfront\n"
            "size\npop\npop\npop\nempty\n"
        ),
        stress(
            "60\n"
            + "\n".join(
                [f"push {i}" for i in range(1, 21)]
                + ["front", "back", "size"]
                + ["pop" for _ in range(20)]
                + ["empty", "pop"]
                + [f"push {i}" for i in range(21, 35)]
                + ["size"]
            )
            + "\n"
        ),
    ]
