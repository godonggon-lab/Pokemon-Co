#!/usr/bin/env bash
# 컨테이너 entrypoint: /code (RO) 의 소스를 /work 로 복사 후 컴파일/실행.
# 컴파일 실패 시 종료코드 100. (judge_core.DockerRunner 가 약속한 값)
# TIME_LIMIT_MS 가 주어지면 coreutils `timeout` 으로 실행 시간을 강제 제한한다.
#   - 시간초과 시 종료코드 124 (timeout 이 SIGTERM 후 SIGKILL 까지 보낸 경우 137 가능)
#   - judge_core.DockerRunner 는 124/137 을 TLE/MLE 로 분류한다.
set -u

cp -r /code/* /work/
cd /work || exit 1

# 시간 제한 (초) — TIME_LIMIT_MS 환경변수에서 환산. 미지정 시 제한 없음.
TL_S=""
if [[ -n "${TIME_LIMIT_MS:-}" ]]; then
  # bash 정수 산술 (소수점 버림). 최소 1초 보장.
  TL_S=$(( TIME_LIMIT_MS / 1000 ))
  if (( TL_S < 1 )); then TL_S=1; fi
fi

run() {
  if [[ -n "$TL_S" ]]; then
    # --kill-after: SIGTERM 후에도 안 끝나면 1초 뒤 SIGKILL
    exec timeout --kill-after=1s --signal=TERM "${TL_S}s" "$@"
  else
    exec "$@"
  fi
}

case "${LANG_NAME}" in
  python)
    run python main.py
    ;;
  javascript)
    run node main.js
    ;;
  cpp)
    if ! g++ -O2 -std=gnu++17 main.cpp -o a.out 2> compile.err; then
      cat compile.err >&2
      exit 100
    fi
    run ./a.out
    ;;
  java)
    if ! javac -encoding UTF-8 Main.java 2> compile.err; then
      cat compile.err >&2
      exit 100
    fi
    run java -cp . Main
    ;;
  *)
    echo "unsupported lang: ${LANG_NAME}" >&2
    exit 2
    ;;
esac
