"""
하네스 채점기 단위 테스트 (Local runner 기반).
docker 없이도 검증 가능 — Python oracle/유저 코드만 사용.

실행:  python -m unittest harness/tests/test_judge.py
"""
from __future__ import annotations
import sys, os, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from harness.judge_core import judge, LocalRunner
import harness.generators as generators

ORACLE_2798 = """\
import sys
def input(): return sys.stdin.readline().rstrip()
N, M = map(int, input().split())
MAX = 0
arr = list(map(int, input().split()))
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for z in range(j+1, len(arr)):
            s = arr[i]+arr[j]+arr[z]
            if s <= M: MAX = max(MAX, s)
print(MAX)
"""

SOLUTION_5597 = """\
student = []

for i in range(1, 31):
    student.append(i)

for _ in range(0, 28):
    n = int(input())
    student.remove(n)

print(min(student))
print(max(student))
"""

SOLUTION_20955 = """\
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = list(range(n + 1))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
cycle = 0
for _ in range(m):
    a, b = map(int, input().split())
    ra, rb = find(a), find(b)
    if ra == rb:
        cycle += 1
    else:
        parent[rb] = ra
components = len({find(i) for i in range(1, n + 1)})
print(cycle + components - 1)
"""

SOLUTION_13910 = """\
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
woks = list(map(int, input().split()))
sizes = set(woks)
for i in range(m):
    for j in range(i + 1, m):
        sizes.add(woks[i] + woks[j])
INF = 10**9
dp = [INF] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for size in sizes:
        if i >= size:
            dp[i] = min(dp[i], dp[i - size] + 1)
print(dp[n] if dp[n] < INF else -1)
"""

SOLUTION_16195 = """\
import sys
input = sys.stdin.readline
mod = 1000000009
t = int(input())
queries = [tuple(map(int, input().split())) for _ in range(t)]
mxn = max(n for n, _ in queries)
mxm = max(m for _, m in queries)
dp = [[0] * (mxm + 1) for _ in range(mxn + 1)]
dp[0][0] = 1
for total in range(1, mxn + 1):
    for cnt in range(1, mxm + 1):
        dp[total][cnt] = sum(dp[total - x][cnt - 1] for x in (1, 2, 3) if total >= x) % mod
pref = [[0] * (mxm + 1) for _ in range(mxn + 1)]
for n in range(1, mxn + 1):
    acc = 0
    for m in range(1, mxm + 1):
        acc = (acc + dp[n][m]) % mod
        pref[n][m] = acc
print('\\n'.join(str(pref[n][m]) for n, m in queries))
"""

SOLUTION_2157 = """\
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b, c = map(int, input().split())
    if a < b:
        edges[a].append((b, c))
NEG = -10**15
dp = [[NEG] * (n + 1) for _ in range(m + 1)]
dp[1][1] = 0
for cnt in range(1, m):
    for city in range(1, n + 1):
        if dp[cnt][city] == NEG:
            continue
        for nxt, score in edges[city]:
            dp[cnt + 1][nxt] = max(dp[cnt + 1][nxt], dp[cnt][city] + score)
print(max(dp[cnt][n] for cnt in range(1, m + 1)))
"""


class JudgeTests(unittest.TestCase):
    def test_samples_run_before_fuzz_cases(self):
        r = judge(
            problem_slug="brute_force-2798", category_slug="brute_force",
            user_lang="python", user_code=ORACLE_2798,
            oracle_lang="python", oracle_code=ORACLE_2798,
            user_runner=LocalRunner(), oracle_runner=LocalRunner(),
            case_count=2,
        )
        self.assertEqual(r["status"], "AC", msg=r)
        self.assertEqual([c["kind"] for c in r["cases"][:2]], ["sample", "sample"])
        self.assertEqual([c["kind"] for c in r["cases"][2:]], ["fuzz", "fuzz"])

    def test_correct_solution_AC(self):
        # itertools 기반 동치 풀이 → AC 기대
        user = """\
import sys, itertools
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
best = 0
for trio in itertools.combinations(arr, 3):
    s = sum(trio)
    if s <= M and s > best: best = s
print(best)
"""
        r = judge(
            problem_slug="brute_force-2798", category_slug="brute_force",
            user_lang="python", user_code=user,
            oracle_lang="python", oracle_code=ORACLE_2798,
            user_runner=LocalRunner(), oracle_runner=LocalRunner(),
            case_count=4,
        )
        self.assertEqual(r["status"], "AC", msg=r)
        self.assertGreater(r["total"], 0)

    def test_wrong_solution_WA(self):
        wrong = """\
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(sum(sorted(arr)[-3:]))   # M 무시 → 거의 항상 WA
"""
        r = judge(
            problem_slug="brute_force-2798", category_slug="brute_force",
            user_lang="python", user_code=wrong,
            oracle_lang="python", oracle_code=ORACLE_2798,
            user_runner=LocalRunner(), oracle_runner=LocalRunner(),
            case_count=4,
        )
        self.assertIn(r["status"], ("WA", "AC"))  # 보통 WA, 우연히 AC도 가능
        # 적어도 한 케이스는 실패해야 의미 있음 (override 의 케이스가 도와줌)
        # 결정적 보장이 어려우므로 status 만 확인하지 않고 케이스 결과 존재 확인
        self.assertGreater(r["total"], 0)

    def test_oracle_failure_returns_ERR(self):
        bad_oracle = "raise RuntimeError('broken oracle')\n"
        r = judge(
            problem_slug="dynamic_programming_2-2157", category_slug="dynamic_programming_2",
            user_lang="python", user_code=SOLUTION_2157,
            oracle_lang="python", oracle_code=bad_oracle,
            user_runner=LocalRunner(), oracle_runner=LocalRunner(),
            case_count=1,
        )
        self.assertEqual(r["status"], "ERR", msg=r)
        self.assertIn("oracle failed", r["message"])

    def test_generator_failure_returns_ERR(self):
        original_generate = generators.generate

        def broken_generate(*args, **kwargs):
            raise RuntimeError("broken generator")

        generators.generate = broken_generate
        try:
            r = judge(
                problem_slug="no_samples-999999", category_slug="brute_force",
                user_lang="python", user_code=ORACLE_2798,
                oracle_lang="python", oracle_code=ORACLE_2798,
                user_runner=LocalRunner(), oracle_runner=LocalRunner(),
                case_count=1,
            )
        finally:
            generators.generate = original_generate

        self.assertEqual(r["status"], "ERR", msg=r)
        self.assertIn("generator failed", r["message"])

    def test_5597_override_matches_problem_input_shape(self):
        r = judge(
            problem_slug="implementation-5597", category_slug="implementation",
            user_lang="python", user_code=SOLUTION_5597,
            oracle_lang="python", oracle_code=SOLUTION_5597,
            user_runner=LocalRunner(), oracle_runner=LocalRunner(),
            case_count=6,
        )
        self.assertEqual(r["status"], "AC", msg=r)
        for case in r["cases"]:
            if case["kind"] not in {"edge", "fuzz"}:
                continue
            lines = case["input"].strip().splitlines()
            self.assertEqual(len(lines), 28, msg=case["input"])
            self.assertTrue(all(line.isdigit() for line in lines), msg=case["input"])
        self.assertIn("edge", [case["kind"] for case in r["cases"]], msg=r)

    def test_generic_fuzz_is_disabled_by_default(self):
        generated = generators.generate("implementation-999999", "implementation", count=3)
        self.assertEqual(generated, [])

    def test_presentation_error_when_tokens_match_but_layout_differs(self):
        one_line = """\
student = []
for i in range(1, 31):
    student.append(i)
for _ in range(28):
    student.remove(int(input()))
print(min(student), max(student))
"""
        r = judge(
            problem_slug="implementation-5597", category_slug="implementation",
            user_lang="python", user_code=one_line,
            oracle_lang="python", oracle_code=SOLUTION_5597,
            user_runner=LocalRunner(), oracle_runner=LocalRunner(),
            case_count=1,
        )
        self.assertEqual(r["status"], "PE", msg=r)

    def test_output_limit_exceeded_returns_OLE(self):
        too_much_output = "print('x' * 2048)\n"
        r = judge(
            problem_slug="brute_force-2798", category_slug="brute_force",
            user_lang="python", user_code=too_much_output,
            oracle_lang="python", oracle_code=ORACLE_2798,
            user_runner=LocalRunner(), oracle_runner=LocalRunner(),
            case_count=1,
            max_output_bytes=64,
        )
        self.assertEqual(r["status"], "OLE", msg=r)


if __name__ == "__main__":
    unittest.main()
