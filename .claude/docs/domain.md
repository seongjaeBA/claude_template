# Domain

## Purpose
Claude Code 프로젝트의 .claude/ 초기 구조와 스킬/템플릿을 제공하는 범용 템플릿 저장소.
클론 후 `/project-init` 또는 `/project-onboard` 스킬로 즉시 프로젝트를 초기화할 수 있다.

## Core Entities

### Skill
- 워크플로우를 정의하는 SKILL.md 파일
- `~/.claude/skills/` 또는 `.claude/skills/`에 위치
- `/skill-name`으로 호출

### Template
- 프로젝트 파일 생성의 기반이 되는 `.tmpl` 또는 `.md` 파일
- 플레이스홀더(`{VARIABLE}`)를 인터뷰 답변으로 치환하여 사용
- `.claude/skills/templates/`에 위치

### Rule
- 코딩 스타일, 에이전트 행동 규칙을 정의
- `.claude/rules/` 또는 `~/.claude/rules/`에 위치
- Claude가 코드 작성 시 자동으로 참조

### Agent
- 독립적으로 실행되는 전문 Claude 인스턴스
- Domain agent(도메인 전담), Reviewer(리뷰), QA(검증) 등 역할별 분류
- Agent memory 파일을 통해 컨텍스트 유지

### Plan
- 구현 로드맵 또는 작업 계획 문서
- `.claude/plans/`에 위치
- 인터뷰 후 `init-roadmap.md` 자동 생성

## Domain Rules
- 모든 생성 파일은 **150줄 이하** (초과 시 분할)
- 템플릿은 스택별 변형 지원 (nodejs, python)
- 스킬은 독립적으로 작동해야 함 (다른 스킬에 의존 금지)
