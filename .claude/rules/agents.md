# Agents (Node.js)

## Domain Agents (Auto-Dispatch)

### home-frontend
- **Scope**: 홈/랜딩 페이지 전용 디자인 + 구현
- **Memory**: `.claude/agent-memory/home-frontend.md` — 반드시 읽고 시작
- **Trigger**: 홈, 랜딩, 메인 페이지, hero section
- **Files**: `src/app/(home)/`, `src/components/home/`
- **Skill**: `frontend-design` 자동 활성화

### dashboard-frontend
- **Scope**: 대시보드 페이지 전용 디자인 + 구현
- **Memory**: `.claude/agent-memory/dashboard-frontend.md` — 반드시 읽고 시작
- **Trigger**: 대시보드, 관리, 통계, 차트
- **Files**: `src/app/dashboard/`, `src/components/dashboard/`

### api-service
- **Scope**: tRPC 라우터 + Supabase/Drizzle 백엔드 로직
- **Memory**: `.claude/agent-memory/api-service.md` — 반드시 읽고 시작
- **Trigger**: API, tRPC, 라우터, 쿼리, mutation, DB
- **Files**: `src/server/`, `src/trpc/`

### 공유 컴포넌트 변경 시
공유 파일 수정 → **관련 도메인 에이전트 병렬 리뷰**

## Reviewers
- code-reviewer: general code review
- security-reviewer: OWASP-based security analysis
- e2e-runner: critical user flows
- tdd-guide: new features, bug fixes
- qa-verifier: TDD 커버리지 충족 검증 (테스트 스펙 대비 실제 TC 비교)

## Optimization (검증 이후 활성화)
- code-simplifier: 중복 제거, 가독성 개선, 불필요 코드 정리
- perf-reviewer: 번들 크기, 렌더링 성능, 메모리 최적화 검토

## Build
- build-error-resolver: npm errors, module issues

## Planning
- planner: complex features, refactoring
- architect: architectural decisions

## Orchestration Rules (자동 라우팅)

### Auto-Dispatch (유저 요청 없이 실행)
| Context | Action |
|---------|--------|
| 홈/랜딩 관련 작업 | `home-frontend` 디스패치, memory 로드 |
| 대시보드 관련 작업 | `dashboard-frontend` 디스패치, memory 로드 |
| API/DB 관련 작업 | `api-service` 디스패치, memory 로드 |
| 공유 컴포넌트 변경 | 관련 도메인 에이전트 **병렬** 리뷰 |
| 새 컴포넌트/기능 구현 요청 | `tdd-guide` **먼저** 디스패치 → 테스트 스펙 작성 후 구현 |
| 코드 작성 완료 | `code-reviewer` 자동 실행 |
| 빌드/에러 발생 | `build-error-resolver` 자동 실행 |
| 3+ 파일 변경 기능 요청 | `.claude/plans/` 에 plan 생성 후 작업 |
| 아키텍처/라이브러리 변경 | `.claude/legacy/` 에 의사결정 기록 작성 후 커밋 |

### TDD 의무화 규칙
1. **코드 작성 전**: `.claude/docs/testing/test-strategy.md` 확인
2. **새 기능/컴포넌트**: `tdd-guide` 에이전트가 테스트 먼저 작성 (RED)
3. **구현 후**: 테스트 통과 확인 (GREEN) → 리팩터링 (REFACTOR)
4. **테스트 없는 코드 커밋 금지**: `code-reviewer`가 테스트 누락 시 CRITICAL 이슈 발행

### QA 검증 파이프라인 (구현 완료 후)
1. `qa-verifier` 디스패치 → `.claude/docs/testing/` 스펙 대비 실제 TC 매핑
2. 누락된 TC 목록 생성 → 자동으로 `tdd-guide`에 전달
3. 커버리지 80%+ 미달 시 커밋 경고
4. 검증 통과 후에만 최적화 단계 진행 허용

### 최적화 흐름 (검증 이후 활성화)
1. QA 검증 통과 → `code-simplifier` 활성화 가능
2. `code-simplifier`: 중복 제거, 가독성 개선
3. `perf-reviewer`: 번들 분석, 렌더링 최적화 제안
4. 최적화는 **기능 완성 + 테스트 통과 이후에만** 실행
5. 최적화 후 **테스트 재실행** 필수 (회귀 방지)

### Worktree 팀 정책
1. **팀 작업 시 worktree 사용 필수** (`isolation: "worktree"`)
2. 각 에이전트는 독립된 git worktree에서 작업 → 충돌 방지
3. 오케스트레이터만 메인 브랜치에서 작업 (설정, 문서 등)
4. 에이전트 완료 후 오케스트레이터가 결과 리뷰 → 머지 결정
5. worktree 작업물은 자동 cleanup (변경 없으면 삭제)

### Team Mode
| Trigger | Agents |
|---------|--------|
| 홈/랜딩 변경 | home-frontend → code-reviewer |
| 대시보드 변경 | dashboard-frontend → code-reviewer |
| API/DB 변경 | api-service → code-reviewer |
| 공유 컴포넌트 변경 | home-frontend + dashboard-frontend (병렬) → code-reviewer |
| Large feature | planner → tdd-guide → (code-reviewer \|\| security-reviewer) |
| Before PR | code-reviewer + security-reviewer parallel |
| Bug fix | tdd-guide → code-reviewer |
| Critical flow | e2e-runner after implementation |
| 기능 완성 후 | qa-verifier → (pass) → code-simplifier |
| 팀 병렬 작업 | 각 에이전트 worktree 격리, 오케스트레이터 리뷰 후 머지 |
| 1-2 file change | single agent only |

### Plan 관리 규칙 (프로젝트 내부 `.claude/plans/`)

#### 자동 생성 트리거
| Trigger | Action |
|---------|--------|
| 3개 이상 파일 변경이 예상되는 기능 요청 | `.claude/plans/{YYYYMMDD}-{slug}.md` 생성 후 작업 시작 |
| 유저가 "계획 세워줘", "plan" 요청 | plan 파일 생성 |
| Phase 기반 작업 (init-roadmap 등) | 해당 plan 파일의 체크리스트 업데이트 |

#### Plan 파일 형식
```markdown
# {기능명}
- **상태**: draft | in-progress | done
- **생성일**: {YYYY-MM-DD}

## 목표
{한 줄 요약}

## 작업 목록
- [ ] 작업 1
- [ ] 작업 2

## 완료 기준
- 기준 1
```

#### 생명주기
1. 작업 시작 시 상태 `in-progress`로 변경
2. 각 작업 완료 시 체크리스트 `[x]` 업데이트
3. 모든 작업 완료 시 상태 `done`으로 변경
4. `done` 상태 plan은 삭제하지 않음 — 이력으로 보존

---

### Legacy (의사결정 기록) 규칙 (프로젝트 내부 `.claude/legacy/`)

#### 자동 생성 트리거
| Trigger | Action |
|---------|--------|
| 아키텍처 변경 (디렉토리 구조, 패턴 변경) | legacy 문서 **반드시** 작성 |
| 라이브러리/프레임워크 교체 또는 추가 | legacy 문서 작성 |
| 기존 방식을 폐기하고 새 방식 도입 | legacy 문서 작성 |
| 성능/보안 이유로 구현 방식 변경 | legacy 문서 작성 |
| 유저가 "왜 이렇게 했지?" 질문할 만한 결정 | legacy 문서 작성 |

#### 파일명 규칙
`.claude/legacy/{YYYYMMDD}-{NNN}-{slug}.md`
- 예: `20260315-001-switch-to-drizzle.md`

#### 작성 전 확인
1. `.claude/legacy/` 내 기존 문서 **Read** — 중복 방지
2. `_template.md` 형식 준수

#### 작성 의무
- 위 트리거에 해당하는 변경 시, **코드 커밋 전에** legacy 문서 작성 필수
- legacy 없이 아키텍처 변경 커밋 시 `code-reviewer`가 CRITICAL 이슈 발행

---

### Memory Protocol
1. 에이전트 디스패치 시 해당 memory 파일 **Read** 후 시작
2. 작업 완료 시 새로운 결정사항/함정을 memory에 **Write**
3. 세션 종료 전 memory 업데이트 확인
