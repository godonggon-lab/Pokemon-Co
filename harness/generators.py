"""
하네스 입력 생성기 (Property-based fuzz generator).

원리:
- BOJ 문제 본문을 가져올 수 없으므로, 카테고리(slug)와 문제번호(id)로
  '이런 모양의 입력이 자주 나온다'는 휴리스틱 템플릿을 적용한다.
- 각 문제마다 hash 시드로 결정적 입력을 N개 생성 (재현성).
- 별도의 problem-specific override 는 harness/overrides/<slug>.py 에 두면
  (gen_inputs(seed) -> List[str]) 함수로 우선 적용된다.

이 파일은 pure-Python, 표준 라이브러리만 사용. judge 컨테이너 안에서 import.
"""
from __future__ import annotations
import importlib.util
import os
import random
from pathlib import Path
from typing import Callable, List

OVERRIDES_DIR = Path(__file__).parent / "overrides"
ENABLE_GENERIC_FUZZ = os.environ.get("JUDGE_ENABLE_GENERIC_FUZZ", "0") == "1"


def _load_override_module(problem_slug: str):
    f = OVERRIDES_DIR / f"{problem_slug}.py"
    if not f.exists():
        return None
    spec = importlib.util.spec_from_file_location(f"override_{problem_slug}", f)
    if spec is None or spec.loader is None:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _load_override(problem_slug: str) -> Callable[[int], List[str]] | None:
    mod = _load_override_module(problem_slug)
    if mod is None:
        return None
    fn = getattr(mod, "gen_inputs", None)
    return fn if callable(fn) else None


def has_override(problem_slug: str) -> bool:
    return (OVERRIDES_DIR / f"{problem_slug}.py").exists()


def replaces_samples(problem_slug: str) -> bool:
    mod = _load_override_module(problem_slug)
    return bool(getattr(mod, "REPLACE_SAMPLES", False)) if mod is not None else False


# ---- 카테고리별 일반 입력 템플릿 -----------------------------------------------
# 시그니처: gen(rng) -> str  (개행 포함 stdin 페이로드)

def _arr_NM(rng: random.Random, *, n_max=20, v_max=20) -> str:
    n = rng.randint(2, n_max)
    m = rng.randint(1, n)
    arr = [rng.randint(1, v_max) for _ in range(n)]
    return f"{n} {m}\n" + " ".join(map(str, arr)) + "\n"


def _arr_N(rng: random.Random, *, n_max=15, v_max=50) -> str:
    n = rng.randint(1, n_max)
    arr = [rng.randint(-v_max, v_max) for _ in range(n)]
    return f"{n}\n" + " ".join(map(str, arr)) + "\n"


def _two_ints(rng: random.Random, *, lo=1, hi=100) -> str:
    return f"{rng.randint(lo, hi)} {rng.randint(lo, hi)}\n"


def _one_int(rng: random.Random, *, lo=1, hi=100) -> str:
    return f"{rng.randint(lo, hi)}\n"


def _grid(rng: random.Random, *, dim_max=8, alphabet="01") -> str:
    n = rng.randint(2, dim_max)
    m = rng.randint(2, dim_max)
    rows = [
        "".join(rng.choice(alphabet) for _ in range(m))
        for _ in range(n)
    ]
    return f"{n} {m}\n" + "\n".join(rows) + "\n"


def _string_only(rng: random.Random, *, max_len=12) -> str:
    L = rng.randint(1, max_len)
    s = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(L))
    return s + "\n"


def _graph_edges(rng: random.Random, *, n_max=8) -> str:
    n = rng.randint(3, n_max)
    m = rng.randint(n - 1, min(n * (n - 1) // 2, n + 4))
    edges = set()
    while len(edges) < m:
        a = rng.randint(1, n); b = rng.randint(1, n)
        if a != b: edges.add((min(a, b), max(a, b)))
    lines = [f"{n} {len(edges)}"]
    for a, b in edges: lines.append(f"{a} {b}")
    return "\n".join(lines) + "\n"


_TEMPLATES = {
    "brute_force":            _arr_NM,
    "binary_search":          _arr_NM,
    "two_pointer":            _arr_NM,
    "prefix_sum":             _arr_NM,
    "data_structure":         _arr_N,
    "data_structure2":        _arr_N,
    "math":                   _two_ints,
    "implementation":         _arr_N,
    "greedy":                 _arr_N,
    "dynamic_programming_1":  _one_int,
    "dynamic_programming_2":  _one_int,
    "dynamic_programming_on_trees": _graph_edges,
    "graph_traversal":        _grid,
    "shortest_path":          _graph_edges,
    "minimum_spanning_tree":  _graph_edges,
    "tree":                   _graph_edges,
    "trie":                   _string_only,
    "string":                 _string_only,
    "simulation":             _grid,
    "backtracking":           _one_int,
    "divide_and_conquer":     _arr_N,
    "disjoint_set":           _graph_edges,
}


def generate(problem_slug: str, category_slug: str, *, count: int = 6, seed: str | None = None) -> List[str]:
    """
    문제별 입력 케이스 N개 생성. 결정적(seed 기반).
    - 우선순위: harness/overrides/<slug>.py:gen_inputs(seed) > 카테고리 템플릿
    """
    override = _load_override(problem_slug)
    if override is not None:
        return list(override(0))[:count]

    if not ENABLE_GENERIC_FUZZ:
        return []

    tmpl = _TEMPLATES.get(category_slug, _arr_N)
    seed_str = seed or problem_slug
    inputs: List[str] = []
    for i in range(count):
        rng = random.Random(f"{seed_str}:{i}")
        inputs.append(tmpl(rng))
    return inputs
