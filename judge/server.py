"""
Judge HTTP server (개발/로컬용 단일 프로세스).
프로덕션에서는 Docker compose 로 띄우고, 사용자 코드 실행은 DockerRunner 가 처리.

POST /judge
  body: { problemSlug, categorySlug, lang, code, oracle: { lang, code } }
  resp: judge_core.judge(...) 결과 JSON

OWASP 관점:
- 사용자 입력은 길이 제한.
- DockerRunner 는 --network=none / --read-only / 메모리·pids·ulimit 제한.
- 호스트 파일시스템에 사용자 코드를 쓰는 임시 디렉토리만 RO 마운트.
"""
from __future__ import annotations
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from harness.judge_core import judge, LocalRunner, DockerRunner

PORT = int(os.environ.get("JUDGE_PORT", "5050"))
USE_DOCKER = os.environ.get("JUDGE_USE_DOCKER", "1") == "1"
MAX_BODY = 256 * 1024


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, payload: dict):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):  # noqa: N802
        if self.path != "/judge":
            return self._send(404, {"status": "ERR", "message": "not found"})
        length = int(self.headers.get("content-length") or 0)
        if length <= 0 or length > MAX_BODY:
            return self._send(413, {"status": "ERR", "message": "body too large"})
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except Exception:
            return self._send(400, {"status": "ERR", "message": "invalid json"})

        try:
            user_runner = DockerRunner() if USE_DOCKER else LocalRunner()
            limits = data.get("limits") or {}
            tl_s = float(limits.get("timeLimitMs", 2000)) / 1000.0
            ml_mb = int(limits.get("memoryLimitMb", 256))
            result = judge(
                problem_slug   = data["problemSlug"],
                category_slug  = data["categorySlug"],
                user_lang      = data["lang"],
                user_code      = data["code"],
                oracle_lang    = data["oracle"]["lang"],
                oracle_code    = data["oracle"]["code"],
                user_runner    = user_runner,
                oracle_runner  = LocalRunner(),
                time_limit_s   = tl_s,
                memory_limit_mb= ml_mb,
            )
            self._send(200, result)
        except KeyError as e:
            self._send(400, {"status": "ERR", "message": f"missing field: {e}"})
        except Exception as e:
            self._send(500, {"status": "ERR", "message": f"judge crashed: {e}"})

    def log_message(self, fmt, *args):  # 콘솔 노이즈 줄이기
        return


def main():
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"[judge] listening on http://127.0.0.1:{PORT}  docker={USE_DOCKER}")
    srv.serve_forever()


if __name__ == "__main__":
    main()
