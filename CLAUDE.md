# claude_template

## Domain
Claude Code 프로젝트의 .claude/ 초기 구조와 스킬/템플릿을 제공하는 범용 템플릿 저장소
Entities: Skill, Template, Rule, Agent, Plan
DoD: 클론 후 /project-init 또는 /project-onboard로 즉시 프로젝트 초기화 가능

## Stack
TypeScript 5.x / Node.js 22 / Next.js / Supabase + Drizzle / Vercel
Package manager: npm
Test: Vitest + Playwright

## Dev Workflow
병렬 에이전트 (2~5개, worktree 격리) | PR: 필수 | CI/CD: Vercel
Quality: Biome (all-in-one) + lefthook

## Docs
- Domain: .claude/docs/domain.md
- Constraints: .claude/docs/constraints.md
- Local checks: .claude/docs/local-checks.md
- Env validation: .claude/docs/env-validation.md
- Backend: .claude/docs/backend/
- Frontend: .claude/docs/frontend/

## Rules
- Common: ~/.claude/rules/
- Stack: .claude/rules/coding-style.md
- Agents: .claude/rules/agents.md

## Agent Memory
- Index: .claude/agent-memory/agents.md
- Domain agents: separate files in .claude/agent-memory/
- Protocol: Read before start → Work → Write updates after completion

## Legacy
Decisions: .claude/legacy/ — read before making architectural changes.
