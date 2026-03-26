# Team Workflow

## Roles

### Orchestrator (메인 에이전트)
- 유저와 직접 커뮤니케이션 유지
- Sub-agent 디스패치, 결과 리뷰, 머지 결정
- 설정/문서 등 메인 브랜치 작업 담당
- 전체 진행 상황 TodoWrite로 추적

### Domain Agents (Sub-agents)
- 특정 도메인(페이지/서비스) 전담
- Memory 파일 읽고 → 작업 → Memory 업데이트
- `frontend-design` 등 도메인 스킬 자동 활성화

### QA Agents
- `qa-verifier`: 테스트 스펙 대비 실제 TC 커버리지 검증
- `tdd-guide`: 누락 TC 작성, RED→GREEN→REFACTOR
- `e2e-runner`: 핵심 사용자 흐름 E2E 실행

### Optimization Agents (게이트 조건부)
- `code-simplifier`: 중복 제거, 가독성 개선
- `perf-reviewer`: 번들 크기, 렌더링 성능 분석

## Worktree 격리 정책

### 필수 규칙
- 팀 병렬 작업 시 각 에이전트는 **worktree 격리** (`isolation: "worktree"`)
- 오케스트레이터만 메인 브랜치에서 작업
- 에이전트 간 파일 충돌 원천 차단

### Worktree 생명주기
1. 에이전트 디스패치 → 자동 worktree 생성 (임시 브랜치)
2. 작업 완료 → 오케스트레이터에게 결과 반환
3. 오케스트레이터 리뷰 → 머지 또는 폐기 결정
4. 변경 없는 worktree → 자동 cleanup

## QA 검증 파이프라인

```
구현 완료
    ↓
qa-verifier 디스패치
    ↓
테스트 스펙(.claude/docs/testing/) 대비 실제 TC 매핑
    ↓
[PASS: 80%+ 커버리지] → 최적화 단계 허용
[FAIL: 커버리지 미달] → 누락 TC 목록 → tdd-guide 디스패치
    ↓
tdd-guide: 누락 TC 작성
    ↓
재검증 (qa-verifier)
```

## 최적화 게이트

### 진입 조건 (모두 충족해야 함)
1. ✅ 기능 구현 완료
2. ✅ qa-verifier 통과 (커버리지 80%+)
3. ✅ 모든 테스트 PASS
4. ✅ 빌드 성공

### 최적화 실행 후
- 테스트 **재실행** 필수 (회귀 방지)
- 최적화로 테스트 실패 시 → 최적화 롤백 또는 수정

## Team Mode 실행 예시

```
# 병렬 3팀 작업
Orchestrator: 설정/문서 (메인 브랜치)
Agent A: 기능 구현 (worktree A)
Agent B: 테스트 작성 (worktree B)

# 완료 후
Orchestrator: Agent A 결과 리뷰 → 머지
Orchestrator: Agent B 결과 리뷰 → 머지
Orchestrator: qa-verifier → 커버리지 검증
Orchestrator: [PASS] → code-simplifier 허용
```
