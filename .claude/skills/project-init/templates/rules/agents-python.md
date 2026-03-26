# Agents (Python)

## Reviewers
- python-reviewer: code review (use over code-reviewer for Python)
- security-reviewer: bandit-based security analysis
- tdd-guide: new features, bug fixes

## Build
- build-error-resolver: pip/poetry/uv errors, import issues

## Planning
- planner: complex features, refactoring
- architect: architectural decisions

## ⛔ MAIN(ORCHESTRATOR) 코드 직접 수정 금지

**main은 항상 유저와의 communication을 유지하며 orchestration만 수행한다.**

| 금지 | 허용 |
|------|------|
| `src/**`, `*.py`, `*.toml`, `*.cfg` 직접 Edit/Write | 유저 응답, 질문 답변, 진행 보고 |
| "단순하니까 내가 해도 되겠지" 판단 | Agent tool로 sub-agent 디스패치 |
| "빨리 끝내려고" 직접 수정 | git merge, 설정 파일 수정, 기록 작업 |
| 코드 리뷰 없이 바로 수정 | 브라우저/도구 확인 작업 |

**코드 변경 요청 처리 절차:**
1. 유저에게 작업 계획 보고
2. 해당 scope의 전담 에이전트를 Agent tool로 디스패치 (`isolation: "worktree"`)
3. 에이전트 완료 후 결과 리뷰 → 머지 → 유저 보고

**"단순한 함수 한 줄"도 예외 없음. 무조건 위임.**

---

## Team Mode
| Trigger | Agents |
|---------|--------|
| Large feature | planner → tdd-guide → (python-reviewer \|\| security-reviewer) |
| Before PR | python-reviewer + security-reviewer parallel |
| Bug fix | tdd-guide → python-reviewer |
| 1-2 file change | single agent only |
