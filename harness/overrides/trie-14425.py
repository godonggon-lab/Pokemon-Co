from harness.cases import edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    words = set(lines[1 : 1 + n])
    count = sum(1 for word in lines[1 + n : 1 + n + m] if word in words)
    return f"{count}\n"


def gen_inputs(_seed):
    cases = [
        "1 3\na\na\nb\nA\n",
        "4 5\nbaekjoon\nstartlink\ncodeplus\nsundaycoding\nbaekjoon\ncodeplus\nmonday\nsundaycoding\nstartlink\n",
        "5 8\na\naa\naaa\nb\nbb\na\naa\naaaa\nb\nbbb\nbb\nc\nA\n",
        "3 4\nhello\nworld\npython\nhello\nhell\nworld\npython\n",
    ]
    out = [edge(case, _solve(case)) for case in cases]
    extra = "6 8\nz\nzz\nabc\nabcd\ncode\njudge\nz\nzz\nzzz\nabc\nab\nabcd\njudge\nJudge\n"
    stress_case = "10 12\n" + "\n".join(f"word{i}" for i in range(10)) + "\n" + "\n".join([
        "word0", "word1", "word9", "word10", "word", "word5",
        "WORD5", "word3", "word8", "x", "word2", "word7"
    ]) + "\n"
    out.append(edge(extra, _solve(extra)))
    out.append(stress(stress_case, _solve(stress_case)))
    return out
