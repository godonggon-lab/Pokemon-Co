# Judge Override 관리 원칙

## 지금은 프로젝트 디렉토리에서 관리한다

현재 단계에서는 `harness/overrides` 안에서 문제별 override를 관리하는 것이 맞다.

이유:

- override는 단순 데이터가 아니라 채점 정책의 일부다.
- 코드 변경과 함께 리뷰, 테스트, 커밋, 롤백되어야 한다.
- 문제 입력 형식이 틀리면 정답 코드가 `oracle failed`로 실패하므로, 앱 코드와 같은 수준으로 관리해야 한다.
- `npm run judge:verify-overrides`로 override 전체를 재검증할 수 있어야 한다.
- C++/Java는 Docker에서 컴파일/실행되므로, 전체 검증은 로컬 단위 테스트보다 오래 걸릴 수 있다.

## 현재 구조

```txt
harness/
  cases.py
  generators.py
  overrides/
    two_pointer-1806.py
    implementation-5597.py
    ...
```

각 override는 다음 형태를 따른다.

```python
from harness.cases import edge, stress


def gen_inputs(_seed: int):
    return [
        edge("input\n"),
        stress("large input\n"),
    ]
```

정답 출력이 명확하고 C++/Java 오라클 실행 의존을 줄이고 싶을 때는 expected output을 함께 둔다.

```python
edge("1\n", "1\n")
```

## 언제 분리할까

나중에 케이스가 커지면 모든 것을 Git repo에 넣는 방식은 무거워진다.

분리 기준:

- 문제별 `.in/.out` 파일이 수천 개 이상으로 늘어날 때
- 큰 stress input이 수 MB 이상이 될 때
- BOJ hidden에 가까운 대량 테스트팩을 운영 서버에서만 사용하고 싶을 때
- 문제/채점 데이터 업데이트를 앱 배포와 따로 하고 싶을 때

그때는 다음처럼 나눈다.

```txt
repo:
  harness/overrides/<slug>.py       # generator, metadata, small edge cases

external storage:
  judge-cases/<slug>/hidden001.in
  judge-cases/<slug>/hidden001.out
  judge-cases/<slug>/stress001.in
  judge-cases/<slug>/stress001.out
```

## 현재 결론

지금은 repo 안에 둔다.

단, 대용량 케이스가 생기는 순간부터는 repo에는 생성기와 작은 edge case만 남기고, 큰 파일은 외부 storage로 옮긴다.
