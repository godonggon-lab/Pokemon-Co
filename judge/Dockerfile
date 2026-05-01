# 다국어 코드 실행용 단일 이미지.
# - Python, Node.js, g++, OpenJDK 17 내장
# - 비루트 사용자, /work tmpfs, /code 읽기전용 마운트
# - entrypoint.sh 가 LANG_NAME 환경변수에 따라 컴파일/실행 분기

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
      python3 python3-minimal \
      g++ make \
      nodejs \
      openjdk-17-jdk-headless \
      ca-certificates \
 && rm -rf /var/lib/apt/lists/* \
 && ln -sf /usr/bin/python3 /usr/local/bin/python

# 비루트 사용자 생성
RUN useradd -m -s /usr/sbin/nologin runner

COPY entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint

USER runner
WORKDIR /work

ENTRYPOINT ["/usr/local/bin/entrypoint"]
