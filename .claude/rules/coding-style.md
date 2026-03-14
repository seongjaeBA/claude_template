# Coding Style (Node.js)

## Standards
- TypeScript strict mode
- All functions typed — no implicit `any`

## Linter / Formatter
- **Biome**: ESLint + Prettier 대체, Rust 기반 고속 실행, 단일 설정 파일
- Hook 명령: `npx biome check --write` (`.claude/settings.json` 참조)
- Pre-commit: lefthook으로 `biome check --write --staged` 자동 실행

## Patterns
- Functional over class-based where possible
- Immutable data: `const`, spread operators, `Object.freeze` for configs
- Async/await over callbacks or raw Promises
- Error handling: explicit try/catch, no swallowing errors

```typescript
// Prefer
const result = await fetchUser(id);
if (!result) throw new Error(`User ${id} not found`);
```

## Security
- No dynamic code execution or dynamic `require()`
- Validate all external input at boundary

## Testing
- Framework: Vitest (단위/통합) + Playwright (E2E)
- Coverage target: 80%+
- E2E: Playwright for critical flows
