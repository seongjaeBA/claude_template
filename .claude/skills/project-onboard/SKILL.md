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

### Step 2.5: Reference & Design Direction (Frontend projects)
*(Skip for backend-only. 나중에 언제든 `/reference-update`로 추가 가능)*

8r. **Reference sites** — 벤치마크 URL 있나요? (없으면 skip)
   - URL 제공 시: WebFetch로 분석 → `docs/references/` 에 저장
   - 분석 항목: 레이아웃, 스크롤 패턴, 네비, 색상/타이포, 인터랙션, 프로젝트 구조(brief/detail)
   - **반영할 패턴** vs **참고만 할 패턴** 명시 기록

9r. **Design direction** — 키워드 or 무드보드? (미니멀, 다크, 글래스모피즘 등)

10r. **Design priority** — 개발 순서 확인:
   - 권장: **레이아웃 → 디자인 시스템 → 인터랙션 → 컴포넌트 → 콘텐츠**
   - 컴포넌트부터 시작하면 전체 흐름이 깨지므로 레이아웃 우선 필수

## Step 3: Scan Existing Structure

After interview, scan for:
- Existing `.claude/` directory (avoid overwriting)
- Existing `docs/references/` (레퍼런스 분석 파일)
- `docs/` or `README.md` for additional context
- Main entry points, key modules

If `.claude/` already exists: confirm before overwriting any files.

## Step 4: Generate .claude/

Use the same output structure as `/project-init`.
Read templates from `~/.claude/skills/project-init/templates/`.

**All files ≤ 150 lines. Split if needed.**

### `.claude/rules/agents.md` — 반드시 포함 섹션
`/project-init`의 agents.md 생성 규칙과 동일. 아래 7개 섹션 필수:
1. **활성 팀 구성 테이블** — 인터뷰 도메인 에이전트 + main/designer/record/code-reviewer/tdd-master-qa
2. **Auto-Dispatch 트리거 테이블** — 각 에이전트 자동 실행 조건
3. **Team Mode 파이프라인** — 도메인 변경 시 에이전트 체인
4. **진행 보고 규칙** — 먹통 금지, 디스패치/완료/에러 시 유저 보고
5. **기록 자동 수행 규칙** — 결정/지시/완료 시 legacy/memory 즉시 기록 (물어보지 말 것)
6. **Memory Protocol** — 디스패치 시 Read, 완료 시 Write
7. **프론트엔드 디자인 우선 규칙** — 레이아웃→디자인시스템→인터랙션→컴포넌트→콘텐츠 (프론트엔드만)

상세 내용은 `/project-init` SKILL.md의 `.claude/rules/agents.md` 섹션 참조.

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
    │   ├── references/       (if reference sites provided)
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
   - 구현 전 → `tdd-master-qa` 디스패치 (RED: TC 먼저 작성)
   - 구현 완료 → `tdd-master-qa` 디스패치 (GREEN 확인 + 커버리지 80%+ 검증)
   - 검증 통과 → 최적화 단계 진입 허용
   - 검증 실패 → 누락 TC 목록 생성 → `tdd-master-qa`가 직접 작성
4. **최적화 게이트**: QA 통과 전 `code-simplifier`/`perf-reviewer` 실행 금지
5. **회귀 방지**: 최적화 후 테스트 재실행 필수

## Post-creation

Report all created/skipped files.
Remind: commit `.claude/` with the project for portability.

## Future Extensions
- `document`: TODO — for documentation projects
- `utility`: TODO — for utility/tooling projects
