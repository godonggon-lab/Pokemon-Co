from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def _check(line: str) -> str:
    steps = line.split()
    broken = [False] * 5
    dip_bad = [False] * len(steps)
    for i, step in enumerate(steps):
        if step == "dip":
            ok = (
                (i >= 1 and steps[i - 1] == "jiggle")
                or (i >= 2 and steps[i - 2] == "jiggle")
                or (i + 1 < len(steps) and steps[i + 1] == "twirl")
            )
            if not ok:
                broken[0] = True
                dip_bad[i] = True
    if len(steps) < 3 or steps[-3:] != ["clap", "stomp", "clap"]:
        broken[1] = True
    if "twirl" in steps and "hop" not in steps:
        broken[2] = True
    if steps and steps[0] == "jiggle":
        broken[3] = True
    if "dip" not in steps:
        broken[4] = True
    fixed = [step.upper() if step == "dip" and dip_bad[i] else step for i, step in enumerate(steps)]
    errors = [str(i + 1) for i, value in enumerate(broken) if value]
    if not errors:
        return "form ok: " + line
    if len(errors) == 1:
        prefix = "form error " + errors[0] + ": "
    else:
        prefix = "form errors " + ", ".join(errors[:-1]) + " and " + errors[-1] + ": "
    return prefix + " ".join(fixed)


def _solve(stdin: str) -> str:
    return "\n".join(_check(line) for line in stdin.splitlines())


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "jiggle dip twirl hop clap stomp clap\n",
        "dip twirl clap stomp clap\n",
        "jiggle dip clap stomp clap\nfoo bar\n",
        "twirl clap stomp clap\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
