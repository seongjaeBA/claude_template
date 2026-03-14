# Agents (Node.js)

## Domain Agents (Auto-Dispatch)

### {domain-agent-1}
- **Scope**: {page/feature} 전용 디자인 + 구현
- **Memory**: `.claude/agent-memory/{domain-agent-1}.md` — 반드시 읽고 시작
- **Trigger**: {keywords that trigger this agent}
- **Files**: {primary files this agent owns}
- **Skill**: `frontend-design` 자동 활성화 (프론트엔드인 경우)

### {domain-agent-2}
- **Scope**: {page/feature} 전용 디자인 + 구현
- **Memory**: `.claude/agent-memory/{domain-agent-2}.md` — 반드시 읽고 시작
- **Trigger**: {keywords that trigger this agent}
- **Files**: {primary files this agent owns}

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
- build-error-resolver: npm/pnpm/yarn errors, module issues

## Planning
- planner: complex features, refactoring
- architect: architectural decisions

## Orchestration Rules (자동 라우팅)

### Auto-Dispatch (유저 요청 없이 실행)
| Context | Action |
|---------|--------|
| 도메인 A 관련 작업 | `{domain-agent-1}` 디스패치, memory 로드 |
| 도메인 B 관련 작업 | `{domain-agent-2}` 디스패치, memory 로드 |
| 공유 컴포넌트 변경 | 관련 도메인 에이전트 **병렬** 리뷰 |
| 새 컴포넌트/기능 구현 요청 | `tdd-guide` **먼저** 디스패치 → 테스트 스펙 작성 후 구현 |
| 코드 작성 완료 | `code-reviewer` 자동 실행 |
| 빌드/에러 발생 | `build-error-resolver` 자동 실행 |

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
| 도메인 A 변경 | {domain-agent-1} → code-reviewer |
| 도메인 B 변경 | {domain-agent-2} → code-reviewer |
| 공유 컴포넌트 변경 | {domain-agent-1} + {domain-agent-2} (병렬) → code-reviewer |
| Large feature | planner → tdd-guide → (code-reviewer \|\| security-reviewer) |
| Before PR | code-reviewer + security-reviewer parallel |
| Bug fix | tdd-guide → code-reviewer |
| Critical flow | e2e-runner after implementation |
| 기능 완성 후 | qa-verifier → (pass) → code-simplifier |
| 성능 이슈 | perf-reviewer → tdd-guide (회귀 테스트) |
| 팀 병렬 작업 | 각 에이전트 worktree 격리, 오케스트레이터 리뷰 후 머지 |
| 1-2 file change | single agent only |

### Memory Protocol
1. 에이전트 디스패치 시 해당 memory 파일 **Read** 후 시작
2. 작업 완료 시 새로운 결정사항/함정을 memory에 **Write**
3. 세션 종료 전 memory 업데이트 확인
