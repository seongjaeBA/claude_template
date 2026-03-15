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

## Team Mode
| Trigger | Agents |
|---------|--------|
| Large feature | planner → tdd-guide → (python-reviewer \|\| security-reviewer) |
| Before PR | python-reviewer + security-reviewer parallel |
| Bug fix | tdd-guide → python-reviewer |
| 3+ 파일 변경 기능 요청 | `.claude/plans/` 에 plan 생성 후 작업 |
| 아키텍처/라이브러리 변경 | `.claude/legacy/` 에 의사결정 기록 작성 후 커밋 |
| 1-2 file change | single agent only |

---

### Plan 관리 규칙 (프로젝트 내부 `.claude/plans/`)

#### 자동 생성 트리거
| Trigger | Action |
|---------|--------|
| 3개 이상 파일 변경이 예상되는 기능 요청 | `.claude/plans/{YYYYMMDD}-{slug}.md` 생성 후 작업 시작 |
| 유저가 "계획 세워줘", "plan" 요청 | plan 파일 생성 |
| Phase 기반 작업 | 해당 plan 파일의 체크리스트 업데이트 |

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

#### 파일명 규칙
`.claude/legacy/{YYYYMMDD}-{NNN}-{slug}.md`

#### 작성 의무
- 위 트리거에 해당하는 변경 시, **코드 커밋 전에** legacy 문서 작성 필수
