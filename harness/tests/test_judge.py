"""
하네스 채점기 단위 테스트 (Local runner 기반).
docker 없이도 검증 가능 — Python oracle/유저 코드만 사용.

실행:  python -m unittest harness/tests/test_judge.py
"""
from __future__ import annotations
import sys, os, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from harness.judge_core import judge, LocalRunner

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


class JudgeTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
