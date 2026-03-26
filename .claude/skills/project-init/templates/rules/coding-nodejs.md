# Coding Style (Node.js)

## Standards
- TypeScript strict mode (if TS project)
- All functions typed — no implicit `any`

## Linter / Formatter (선택)
- **ESLint + Prettier**: 전통적 조합, 풍부한 플러그인 생태계
- **Biome**: ESLint + Prettier 대체, Rust 기반 고속 실행, 단일 설정 파일
- **oxlint**: Rust 기반 빠른 린터 (ESLint 규칙 호환), Prettier와 병행 사용
- 프로젝트 선택에 따라 hook 명령어 조정 (`.claude/settings.json` 참조)

## Patterns
- Functional over class-based where possible
- Immutable data: `const`, spread operators, `Object.freeze` for configs
- Async/await over callbacks or raw Promises
- Error handling: explicit try/catch, no swallowing errors

```typescript
// Prefer
const result = await fetchUser(id);
if (!result) throw new Error(`User ${id} not found`);

// Over
fetchUser(id).then(r => ...).catch(e => ...)
```

## Security
- Never `eval()` or dynamic `require()`
- Validate all external input at boundary
- Use `helmet` for HTTP headers (Express projects)

## Testing
- Framework: Jest (or Vitest for Vite projects)
- Coverage target: 80%+
- E2E: Playwright for critical flows
