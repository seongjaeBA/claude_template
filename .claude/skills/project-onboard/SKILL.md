---
name: project-onboard
description: Onboard Claude to an existing project - auto-detect stack, interview for domain
allowed-tools: Write, Read, Bash, Glob
---

# project-onboard

Initialize `.claude/` for an **existing** project by analyzing the codebase first.
For new projects, use `/project-init` instead.

## Step 1: Auto-detect Stack

Read the following files if present:
- `package.json`, `package-lock.json`, `pnpm-lock.yaml`
- `pyproject.toml`, `setup.py`, `requirements.txt`, `Pipfile`
- `Makefile`, `Dockerfile`, `docker-compose.yml`
- `*.config.{js,ts}` (eslint, jest, vite, etc.)
- `*.toml`, `*.cfg`

Summarize detected stack to user:
> "Detected: Python 3.11 + FastAPI + PostgreSQL + pytest. Confirm or correct?"

Wait for confirmation before proceeding.

## Step 2: Domain Interview

Ask Stage 1 questions only (tech is already known):

1. Project purpose — one sentence
2. Core business entities (3-5 names)
3. Key constraints / non-functional requirements
4. Definition of Done

Also ask:
5. Is this backend-only, frontend-only, or fullstack?
6. Any domain-specific terminology Claude should know?
7. **Domain agents**: What are the major pages/features/services?
   - Frontend: per-page agents (e.g., `home-frontend`, `dashboard-frontend`)
   - Backend: per-service agents (e.g., `auth-service`, `payment-service`)
   - Each gets a separate memory file in `.claude/agent-memory/`

## Step 3: Scan Existing Structure

After interview, scan for:
- Existing `.claude/` directory (avoid overwriting)
- `docs/` or `README.md` for additional context
- Main entry points, key modules

If `.claude/` already exists: confirm before overwriting any files.

## Step 3.5: History Recovery (기존 프로젝트 이력 복원)

기존 프로젝트는 `.claude/plans/`와 `.claude/legacy/`가 비어있을 수 있다.
커밋 히스토리에서 프로젝트 맥락을 복원한다.

### 3.5.1 커밋 로그 분석
```bash
# 최근 50개 커밋 요약
git log --oneline -50

# 주요 아키텍처 변경 탐지 (대규모 변경 커밋)
git log --shortstat -20 --format="%h %s" | head -60

# 의존성 변경 이력
git log --oneline --follow -- package.json pyproject.toml requirements.txt | head -20

# 디렉토리 구조 변경 이력
git log --diff-filter=A --name-only --format="%h %s" -- "*.config.*" "*/index.*" | head -30
```

### 3.5.2 Legacy 자동 생성
커밋 로그에서 다음 패턴을 감지하면 `.claude/legacy/` 문서를 자동 생성:

| 커밋 패턴 | 생성할 Legacy |
|-----------|--------------|
| 프레임워크/라이브러리 마이그레이션 커밋 | `{date}-001-migrate-{from}-to-{to}.md` |
| 대규모 리팩토링 (10+ 파일 변경) | `{date}-002-refactor-{slug}.md` |
| 의존성 교체 (package.json 주요 변경) | `{date}-003-replace-{old}-with-{new}.md` |
| 디렉토리 구조 변경 | `{date}-004-restructure-{slug}.md` |

각 legacy 문서에 포함할 내용:
- **현상**: 커밋 메시지 + diff 요약
- **의사결정**: 커밋 컨텍스트에서 추론
- **참조**: 해당 커밋 해시

### 3.5.3 Plan 상태 복원
```bash
# 미완성 기능 탐지 (TODO, FIXME, WIP 커밋)
git log --oneline --grep="WIP\|TODO\|wip\|fixme" -10

# 최근 활발한 작업 영역
git log --name-only --format="" -10 | sort | uniq -c | sort -rn | head -10
```

미완성 기능이 발견되면:
- `.claude/plans/{date}-recover-{feature}.md` 생성
- 상태: `in-progress`
- 관련 파일 목록 + 남은 작업 추론

### 3.5.4 결과 보고
복원된 이력을 유저에게 보고:
> "커밋 로그에서 N개의 아키텍처 결정과 M개의 진행 중 작업을 발견했습니다."
> - Legacy: {생성된 문서 목록}
> - Plans: {복원된 plan 목록}
> "내용을 검토하고 수정이 필요하면 알려주세요."

## Step 4: Generate .claude/

Use the same output structure as `/project-init`.
Read templates from `~/.claude/skills/project-init/templates/`.

**All files ≤ 150 lines. Split if needed.**

```
{project}/
├── CLAUDE.md
└── .claude/
    ├── settings.json
    ├── rules/
    │   ├── agents.md
    │   └── coding-style.md
    ├── docs/
    │   ├── domain.md
    │   ├── constraints.md
    │   ├── testing/
    │   │   └── test-strategy.md
    │   ├── backend/          (if applicable)
    │   └── frontend/         (if applicable)
    ├── plans/
    ├── agent-memory/
    │   ├── agents.md              (index)
    │   ├── {domain-agent-1}.md    (per domain)
    │   └── {domain-agent-2}.md    (per domain)
    └── legacy/
        └── _template.md
```

## Step 5: Test Coverage Audit

Scan existing codebase for test status:
1. Detect test directories (`__tests__/`, `tests/`, `*.test.*`, `*.spec.*`)
2. Check test config files (`vitest.config.*`, `jest.config.*`, `playwright.config.*`)
3. Run test command if available (`npm test`, `pytest`, etc.) and report results
4. Calculate approximate coverage: files with tests vs total source files
5. Generate `.claude/docs/testing/test-strategy.md` using `templates/testing-strategy.md`
   - Fill with detected test tools and actual coverage status
   - Flag untested critical paths (pages, API routes, utils)

## Step 6: Workflow Setup

Generate `.claude/docs/workflow/team-workflow.md`:
1. **Worktree 격리 정책**: 팀 병렬 작업 시 각 에이전트 worktree 사용 필수
2. **오케스트레이터 역할 정의**: 유저와 직접 소통, sub-agent 결과 리뷰/머지
3. **QA 검증 파이프라인**:
   - 구현 완료 → `qa-verifier` 디스패치 (테스트 스펙 대비 TC 커버리지 검증)
   - 검증 통과 → 최적화 단계 진입 허용
   - 검증 실패 → 누락 TC 목록 생성 → `tdd-guide`에 전달
4. **최적화 게이트**: QA 통과 전 `code-simplifier`/`perf-reviewer` 실행 금지
5. **회귀 방지**: 최적화 후 테스트 재실행 필수

## Step 7: Plan/Legacy 초기화 확인

생성된 `.claude/` 구조에 다음이 포함되었는지 최종 확인:

1. **`.claude/plans/`** — Step 3.5에서 복원된 plan 파일 또는 빈 디렉토리
2. **`.claude/legacy/`** — Step 3.5에서 복원된 legacy 파일 + `_template.md`
3. **`CLAUDE.md`** — Plans/Legacy 섹션에 세션 시작 시 Read 프로토콜 포함
4. **`.claude/rules/agents.md`** — Auto-Dispatch 테이블에 plan/legacy 트리거 포함

누락된 항목이 있으면 자동 생성.

## Post-creation

Report all created/skipped files.
Report recovered history (legacy/plan files from commit log).
Remind: commit `.claude/` with the project for portability.

## Future Extensions
- `document`: TODO — for documentation projects
- `utility`: TODO — for utility/tooling projects
