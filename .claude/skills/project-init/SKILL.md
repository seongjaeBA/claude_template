---
name: project-init
description: New project initialization - structured interview then .claude/ scaffold
allowed-tools: Write, Read, Bash, Glob
---

# project-init

Initialize `.claude/` structure for a **new** project via 3-stage interview.
For existing projects, use `/project-onboard` instead.

## Arguments
`$ARGUMENTS`: optional stack hint (`python` | `nodejs`). Skips Stage 3 tech questions if provided.

## Interview Protocol

Ask each question **one at a time**. Wait for answer before proceeding.

### Stage 1: Business Domain
1. Project purpose — one sentence
2. Core business entities (3-5 names)
3. Key constraints / non-functional requirements
4. Definition of Done

### Stage 1.5: Reference & Design Direction (Frontend projects)
*(Skip for backend-only. 나중에 언제든 `/reference-update`로 추가 가능)*

5r. **Reference sites** — 벤치마크 URL 있나요? (없으면 skip)
   - URL 제공 시: WebFetch로 분석 → `docs/references/` 에 저장
   - 분석 항목: 레이아웃, 스크롤 패턴, 네비, 색상/타이포, 인터랙션, 프로젝트 구조(brief/detail)
   - **반영할 패턴** vs **참고만 할 패턴** 명시 기록

6r. **Design direction** — 키워드 or 무드보드? (미니멀, 다크, 글래스모피즘 등)

7r. **Design priority** — 개발 순서 확인:
   - 권장: **레이아웃 → 디자인 시스템 → 인터랙션 → 컴포넌트 → 콘텐츠**
   - 컴포넌트부터 시작하면 전체 흐름이 깨지므로 레이아웃 우선 필수

### Stage 2: Dev Workflow
5. Solo or team? (if team: size)
6. PR / code review required?
7. Code quality tools:
   - **Linter**: ESLint | oxlint | Biome (all-in-one) | none
   - **Formatter**: Prettier | Biome | none
   - **Note**: Biome replaces both ESLint + Prettier
   - **Local automation**: husky + lint-staged | lefthook | manual only
8. CI/CD pipeline?

### Stage 3: Tech Stack
*(Skip if $ARGUMENTS provided — confirm auto-detected values instead)*

9. Language / runtime version

10. Framework — present trade-offs neutrally:
    - **Next.js**: SSR/SSG/ISR/CSR all supported, Vercel-optimized. Higher complexity.
    - **Astro**: Content-focused static sites, islands architecture. Multi-framework UI.
    - **SvelteKit**: Minimal bundle, low learning curve, full-stack.
    - **Remix (= React Router v7)**: Full-stack, Web Fetch API based, great DX.
    - **Vite + React**: Pure SPA only (no SSR needed). Simplest setup.
    - *Clarify*: SSG ≠ no interactivity. SSG pre-generates HTML; client JS/animations work normally.

11. Package manager: npm | pnpm | yarn | bun
    - *Multi-OS/PC environments*: npm is most portable. bun has limited Windows native support.

12. DB / external services:
    - 12a. What DB or external services? (Supabase, PlanetScale, Turso, none, etc.)
    - 12b. **ORM** (if DB used): Prisma | Drizzle | Kysely | none (raw queries)
      - Prisma: mature, great DX, heavier codegen
      - Drizzle: lightweight, SQL-like syntax, serverless-friendly
      - Kysely: type-safe SQL builder, no codegen

13. API / RPC layer (if backend exists):
    - **Framework native**: Next.js API Routes / Remix loaders / SvelteKit endpoints
    - **tRPC**: Type-safe RPC, best for full-stack TypeScript monorepos
    - **REST**: Manual fetch, OpenAPI optional
    - **GraphQL**: Apollo / Pothos (high complexity, justified for complex graph data)

14. Test tools: Vitest | Jest | Playwright (E2E) | none

15. Observability — LogTape ≠ Sentry (different purposes):
    - **none**: Small/personal projects
    - **LogTape**: Lightweight structured logging library (local + server, free)
    - **Sentry**: Error tracking + performance monitoring platform (production-focused, freemium)
    - **Both**: LogTape for structured logs + Sentry for error tracking

16. Environment variable validation:
    - **none**: Plain `process.env` access
    - **t3-env**: Zod-based, runtime + build-time validation (recommended for Vercel deployments)
    - **dotenv-safe**: `.env.example`-based validation

17. Deployment target (local / Docker / Vercel / other Cloud)

---

## File Generation

After interview, create the following. **All files ≤ 150 lines. Split if needed.**

### CLAUDE.md (project root)
Index file. Reference `.claude/docs/` for details. Do NOT embed full content here.

Template: read `templates/CLAUDE.md.tmpl` and fill with interview answers.

### .claude/settings.json
Read `templates/settings-{stack}.json` for the detected stack.
Replace `{linter}` and `{formatter}` with interview answers.
- If Biome selected: use single `biome check --write` command instead of separate eslint/prettier hooks
- If oxlint selected: use `oxlint` for lint, keep Prettier for format

### .claude/rules/agents.md
Read `templates/rules/agents-{stack}.md` and fill stack-specific values.

**반드시 포함해야 하는 섹션 (템플릿에 없으면 직접 생성):**

#### 1. 활성 팀 구성 테이블
인터뷰에서 식별된 도메인 에이전트 + 아래 필수 에이전트:
| Agent | 역할 | worktree | memory |
|-------|------|----------|--------|
| **main (orchestrator)** | 전체 조율, 유저 보고, 머지, 기록 관리 | - (메인) | - |
| **{domain-agent-1}** | (인터뷰에서 결정) | ✅ | `.claude/agent-memory/{name}.md` |
| **designer** | 디자인 시스템, 토큰, 시각 일관성 검증 | ✅ | - |
| **record** | legacy/memory/plan 기록 자동 수행 | - (메인) | `.claude/agent-memory/agents.md` |
| **code-reviewer** | 코드 리뷰 (lint, 패턴, 접근성) | ✅ | - |
| **tdd-master-qa** | TDD TC 작성 + 커버리지 80%+ 검증 + QA | ✅ | `.claude/docs/testing/` |

- `designer`는 프론트엔드 프로젝트에서만 포함
- 백엔드 전용 시 `designer` 대신 `api-reviewer` 고려

#### 2. Auto-Dispatch 트리거 테이블
```markdown
### Auto-Dispatch (유저가 요청 안해도 실행)
| Context | Action |
|---------|--------|
| {domain} 작업 | `{domain-agent}` 디스패치 (memory 로드) |
| 새 컴포넌트/색상/타이포 변경 | `designer` 디스패치 |
| 코드 작성 완료 | `code-reviewer` 자동 실행 |
| 결정/지시/완료 발생 | `record` 자동 실행 |
| 구현 전 | `tdd-master-qa` 디스패치 (RED: TC 먼저) |
| 구현 완료 후 | `tdd-master-qa` 디스패치 (GREEN + 커버리지) |
| 버그/에러 발생 | `build-error-resolver` 자동 실행 |
```

#### 3. Team Mode 파이프라인
```markdown
### Team Mode
| Trigger | Agents |
|---------|--------|
| {domain} 변경 | {domain-agent} → designer → code-reviewer |
| 새 기능 추가 | tdd-master-qa (RED) → {domain-agent} (GREEN) → designer → code-reviewer → tdd-master-qa (QA) |
| 기능 완성 후 | tdd-master-qa (QA pass 80%+) → code-simplifier |
| 팀 병렬 작업 | 각 에이전트 worktree 격리 |
| 모든 작업 | `record` 항상 병렬 실행 |
```

#### 4. 진행 보고 규칙 (CRITICAL)
```markdown
### 진행 보고 규칙 (CRITICAL — 먹통 금지)
| 시점 | 보고 내용 |
|------|----------|
| 에이전트 디스패치 시 | "Agent X 시작: [작업 내용]" 유저에게 알림 |
| 각 단계 완료 시 | 결과 요약 + 다음 단계 안내 |
| 에러/블로커 발생 시 | 즉시 유저에게 보고 + 대안 제시 |
| 긴 작업 (30초+) | 중간 상태 보고 |
| 세션 재개 시 | 즉시 현재 상태 + 중단된 지점 보고 |
| background agent 완료 시 | 결과 요약 유저에게 전달 |

**원칙**: 유저가 "지금 뭐하는 중?" 이라고 물어봐야 하는 상황 금지.
```

#### 5. 기록 자동 수행 규칙 (CRITICAL)
```markdown
### 기록 자동 수행 규칙 (CRITICAL — 물어보지 말고 실행)
| 트리거 | 자동 수행 | 대상 파일 |
|--------|----------|----------|
| 아키텍처/디자인 결정 | legacy 기록 작성 | `.claude/legacy/{date}-{seq}-{topic}.md` |
| 유저 지시 | legacy 기록 작성 | `.claude/legacy/{date}-{seq}-{topic}.md` |
| 브레인스토밍/스펙 확정 | agent-memory + legacy | 해당 파일 |
| 구현 계획 확정 | plan 파일 작성 | `.claude/plans/{topic}.md` |
| 작업 완료 | agent-memory TODO 업데이트 | 해당 agent-memory |
| 세션 종료/compact | 미기록 항목 일괄 기록 | legacy + agent-memory |

**원칙**: 유저에게 "기록 남길까요?" 물어보는 상황 금지.
```

#### 6. Memory Protocol
```markdown
### Memory Protocol
1. 에이전트 디스패치 시 해당 memory 파일 **Read** 후 시작
2. 작업 완료 시 새로운 결정사항/함정을 memory에 **Write**
3. 세션 종료 전 memory 업데이트 확인
```

#### 7. 프론트엔드 디자인 우선 규칙 (프론트엔드 프로젝트만)
```markdown
### 프론트엔드 디자인 우선 규칙 (CRITICAL)
1. **레이아웃** → 2. **디자인 시스템** → 3. **인터랙션** → 4. **컴포넌트** → 5. **콘텐츠**
위반 금지: 컴포넌트부터 시작하면 레이아웃 깨짐 → 전면 재작업.
```

### .claude/rules/coding-style.md
Read `templates/rules/coding-{stack}.md` and adapt linter/formatter choices from interview.

### .claude/docs/domain.md
Entities, domain rules, invariants. **Project-specific only** — omit general programming concepts.

### .claude/docs/constraints.md
Non-functional requirements, hard limits, compliance rules.
Include local quality check commands based on chosen tools.

### .claude/docs/local-checks.md
Read `templates/local-checks-nodejs.md` (or python equivalent).
Adapt commands to match the chosen linter/formatter/test tools.

### .claude/docs/backend/ (if project has backend)
- `api-endpoints.md` — endpoint list + routing rules
- `api-business.md` — business logic rules core to the domain
- `boilerplate.md` — reusable code patterns for this project
  - Include ORM setup snippet if ORM selected
  - Include tRPC router scaffold if tRPC selected
  - Include t3-env schema if t3-env selected
  - Include Sentry/LogTape init if observability selected

### .claude/docs/frontend/ (if project has frontend)
- `design.md` — design tokens, color system, spacing (no code)
- `components.md` — component patterns + code guide

### .claude/docs/references/ (if reference sites provided)
- `{site-name}.md` — per-reference analysis (layout, scroll, nav, design, interaction)
- `design-direction.md` — 반영할 패턴 요약 + 디자인 키워드 + 개발 순서
- **이 디렉토리는 프로젝트 진행 중 언제든 추가 가능** (유저가 새 레퍼런스 제공 시)

### .claude/docs/testing/ (always generate)
Read `templates/testing-strategy.md` and fill with interview answers (Stage 2 Q14).
- `test-strategy.md` — test pyramid, coverage target, TDD rules
- Backend projects: add `backend-test-specs.md` (API endpoint tests, service layer tests)
- Frontend projects: add `frontend-test-specs.md` (component tests, page rendering, interaction)
- Fullstack: generate both

### .claude/docs/observability.md (if Sentry or LogTape selected)
Read `templates/observability.md` and fill with chosen tools.

### .claude/docs/env-validation.md (if t3-env or dotenv-safe selected)
Read `templates/env-validation.md` and fill with chosen approach.

### .claude/legacy/_template.md
Copy `templates/legacy/_template.md` as-is.

### .claude/agent-memory/agents.md
Read `templates/agent-memory-{stack}.md` and fill stack-specific agents.
Index file — domain agents reference separate memory files.

### .claude/agent-memory/{domain-agent}.md (per domain agent)
Read `templates/agent-memory-domain.md` as template.
Create one file per identified domain agent from interview.
**Frontend projects**: create per-page agents (e.g., `home-frontend.md`, `dashboard-frontend.md`).
**Backend projects**: create per-service agents (e.g., `auth-service.md`, `payment-service.md`).
Fill with initial design decisions, key files, and empty pitfalls section.

### .claude/plans/ (empty directory)
Claude creates plan files here during work. No initial file.

### .claude/docs/workflow/ (always generate)
- `team-workflow.md` — 팀 작업 규칙:
  - Worktree 격리 정책 (병렬 에이전트는 반드시 worktree 사용)
  - 오케스트레이터 역할 (유저 소통, 리뷰, 머지 결정)
  - QA 검증 파이프라인 (구현 → qa-verifier → 최적화)
  - 최적화 게이트 (테스트 통과 전 최적화 금지)

---

### .claude/plans/init-roadmap.md (신규)
인터뷰 결과를 바탕으로 초기 개발 로드맵 생성. 포함 내용:
- **Phase 0**: 프로젝트 초기화 (패키지 설치, 설정 파일)
- **Phase 1~N**: 핵심 기능 구현 순서 (의존성 기준으로 정렬)
- 각 Phase마다: 목표, 작업 목록, 완료 기준
- 기술적 전제 조건 (외부 서비스 계정, API 키 등)

---

## Post-creation

Report all created files with one-line description each.
Show the roadmap summary from `.claude/plans/init-roadmap.md`.
Remind: `.claude/` should be committed with the project for portability.
