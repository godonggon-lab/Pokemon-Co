from __future__ import annotations

from typing import Literal, TypedDict

CaseKind = Literal["edge", "stress", "fuzz"]


class GeneratedCase(TypedDict, total=False):
    input: str
    kind: CaseKind
    expected: str


def edge(stdin: str, expected: str | None = None) -> GeneratedCase:
    return _case(stdin, "edge", expected)


def stress(stdin: str, expected: str | None = None) -> GeneratedCase:
    return _case(stdin, "stress", expected)


def fuzz(stdin: str, expected: str | None = None) -> GeneratedCase:
    return _case(stdin, "fuzz", expected)


def _case(stdin: str, kind: CaseKind, expected: str | None) -> GeneratedCase:
    item: GeneratedCase = {"input": stdin, "kind": kind}
    if expected is not None:
        item["expected"] = expected
    return item
