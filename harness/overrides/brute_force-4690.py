from harness.cases import edge


REPLACE_SAMPLES = True


def _solve() -> str:
    out = []
    for a in range(2, 101):
        a3 = a ** 3
        for b in range(2, a):
            for c in range(b + 1, a):
                for d in range(c + 1, a):
                    if b ** 3 + c ** 3 + d ** 3 == a3:
                        out.append(f"Cube = {a}, Triple = ({b},{c},{d})")
    return "\n".join(out) + "\n"


def gen_inputs(_seed):
    return [edge("", _solve())]
