# Constraints

## File Size
- 모든 생성 파일: **150줄 이하**
- 초과 시 반드시 분할

## Directory Structure
- `.claude/` 디렉토리 구조 규칙 준수
- 템플릿 독립성 유지 (상호 의존 금지)

## Quality Gates
- PR 필수 — 직접 main 커밋 금지
- Biome check 통과 필수 (lint + format)
- TypeScript strict mode — `any` 타입 금지
- 테스트 커버리지 80%+ 유지

## Local Quality Check Commands
```bash
# Lint + Format (Biome all-in-one)
npx biome check --write .

# TypeScript type check
npx tsc --noEmit

# Unit + Integration tests
npx vitest run

# E2E tests
npx playwright test

# Coverage report
npx vitest run --coverage
```

## Deployment
- Vercel 자동 배포
- t3-env로 환경변수 검증 (빌드 타임)
- Supabase 환경변수 필수: `DATABASE_URL`, `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`

## Security
- 환경변수를 클라이언트 번들에 노출 금지 (`NEXT_PUBLIC_` 접두사만 허용)
- Supabase service role key는 서버 전용
