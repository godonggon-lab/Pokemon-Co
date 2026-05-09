# Phase 09. Python/C++ 제출 런타임 보장

## 목표

모든 문제에서 기본 제출 언어로 `python`과 `cpp`를 사용할 수 있게 만든다.

여기서 중요한 구분은 두 가지다.

- 사용자 제출 가능 언어: 사용자가 에디터에서 선택하고 judge 서버가 실행할 수 있는 언어
- oracle 소스 언어: 채점 expected output을 만들기 위해 내부에서 사용하는 정답 코드 언어

문제마다 Python/C++ 정답 소스가 모두 있어야 Python/C++ 제출이 가능한 것은 아니다.
oracle은 Java/C++/Python 중 하나만 있어도 되고, override에 expected output이 있으면 oracle 실행 자체를 생략할 수 있다.

## 현재 상태

프론트/API는 이미 모든 문제에 대해 다음 제출 언어를 열어둔다.

```txt
python
cpp
java
```

Docker runner image도 다음 런타임을 포함한다.

```txt
python3
g++
OpenJDK 17
```

따라서 운영 기준으로는 `JUDGE_USE_DOCKER=1`과 `dongjun-coderunner:latest` image가 준비되어 있으면 모든 문제에서 Python/C++ 제출을 받을 수 있다.

## 소스 커버리지 현황

2026-05-09 기준 `data/problems.json` 기준:

```txt
total: 362
python source 있음: 194
cpp source 있음: 187
python/cpp 둘 다 있음: 48
python/cpp 둘 다 없음: 29
```

주의:

- 이 수치는 “정답 소스가 어떤 언어로 저장되어 있는가”를 뜻한다.
- “사용자가 Python/C++로 제출할 수 있는가”와는 다르다.
- Python/C++ 소스가 없는 문제도 Java oracle 또는 override expected output으로 채점할 수 있다.

## 운영 조건

운영 서버에서는 다음 조건을 기본값으로 둔다.

```env
JUDGE_USE_DOCKER=1
CODERUNNER_IMAGE=dongjun-coderunner:latest
```

C++ 제출은 로컬 `g++`에 의존하지 않고 Docker container 안의 `g++`로 컴파일되어야 한다.
그래야 Windows 개발 환경, Linux 운영 환경, 로컬 설치 상태 차이와 무관하게 동일하게 동작한다.

## 추가한 점검 명령

```bash
npm run judge:lang-audit
```

이 명령은 다음을 확인한다.

- API가 `python`, `cpp`를 허용하는지
- Playground가 `python`, `cpp`를 보여주는지
- Dockerfile에 `python3`, `g++`가 포함되어 있는지
- entrypoint가 `python`, `cpp` 실행 분기를 갖고 있는지
- 현재 로컬 머신에 `python`, `g++`, `docker` 명령이 있는지
- 문제별 oracle/source 언어 분포가 어떤지

## 완료 기준

- `npm run judge:lang-audit`에서 `allProblemsAcceptPythonCpp: true`
- `npm run judge:coverage`에서 `missingCases: 0`
- 운영 환경에서 `JUDGE_USE_DOCKER=1`
- coderunner image build 완료
- Python 제출과 C++ 제출 smoke test 통과

## 다음 작업

1. Docker Desktop 또는 운영 Linux 서버에서 `dongjun-coderunner:latest` image를 build한다.
2. judge 서버를 `JUDGE_USE_DOCKER=1`로 실행한다.
3. Python/C++ 각각 간단한 문제 하나씩 제출해서 `AC`를 확인한다.
4. 이후 일반 sample-only 139개 override를 계속 줄인다.
