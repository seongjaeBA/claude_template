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
| 1-2 file change | single agent only |
