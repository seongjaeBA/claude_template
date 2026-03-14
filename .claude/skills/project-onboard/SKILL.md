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

## Post-creation

Report all created/skipped files.
Remind: commit `.claude/` with the project for portability.

## Future Extensions
- `document`: TODO — for documentation projects
- `utility`: TODO — for utility/tooling projects
