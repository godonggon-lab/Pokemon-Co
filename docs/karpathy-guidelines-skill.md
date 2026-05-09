---
name: karpathy-guidelines
description: Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria.
source: https://github.com/forrestchang/andrej-karpathy-skills
license: MIT
---

# Karpathy Guidelines For DongJun

이 문서는 `forrestchang/andrej-karpathy-skills`의 `CLAUDE.md`와
`skills/karpathy-guidelines/SKILL.md` 내용을 DongJun 프로젝트에서 참고하기 쉽게 정리한 것이다.

## 핵심 원칙

1. **Think Before Coding**
   - 코드 수정 전에 목표, 가정, 트레이드오프를 먼저 정리한다.
   - 불명확한 요구사항은 추측으로 크게 밀고 가지 않고 필요한 질문을 한다.

2. **Simplicity First**
   - 현재 문제를 해결하는 가장 단순한 구현을 우선한다.
   - 미래 확장 가능성만으로 불필요한 추상화나 프레임워크를 추가하지 않는다.

3. **Surgical Changes**
   - 필요한 파일과 필요한 줄만 수정한다.
   - 사용자가 만든 변경사항이나 관련 없는 작업물을 되돌리지 않는다.
   - 기존 스타일과 구조를 우선 따른다.

4. **Goal-Driven Execution**
   - 완료 기준을 명확히 잡고, 그 기준을 검증할 수 있는 테스트나 명령을 실행한다.
   - 큰 작업은 phase 또는 batch로 나누고, 각 batch의 결과를 문서화한다.

## DongJun에 적용하는 방식

- judge 관련 작업은 “대충 통과”가 아니라 재현 가능한 케이스와 검증 명령을 기준으로 진행한다.
- override는 특정 언어가 아니라 입력/출력 계약을 강화하는 방향으로 만든다.
- 문서화는 사용자가 운영과 다음 개발 단계를 이해할 수 있게 한국어로 작성한다.
- 배포 관련 작업은 로컬 개발, Docker judge, Linux VM/Nginx 운영 환경을 구분해서 설명한다.

## 적용 범위

루트의 `AGENTS.md`가 Codex가 이 프로젝트를 다룰 때 우선 참고할 실행 규칙이다.
이 파일은 원본 skill의 의도와 기준을 보존하기 위한 문서형 사본이다.
