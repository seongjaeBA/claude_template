# Test Strategy

## Test Pyramid
- **Unit**: Vitest — 컴포넌트, 유틸, 데이터 모델, 순수 함수
- **Integration**: 페이지 렌더링, tRPC 프로시저, Drizzle 쿼리, 미들웨어
- **E2E**: Playwright — 핵심 사용자 흐름 (인증, 메인 페이지, 네비게이션)

## Coverage Target: 80%+

## TDD Rules (필수)
1. 새 컴포넌트/기능 → **테스트 먼저 작성** (RED → GREEN → REFACTOR)
2. PR 전 `npx vitest run` 통과 필수
3. 테스트 없는 새 코드 커밋 금지
4. E2E는 핵심 흐름만 유지 (과도한 E2E 지양)

## Test File Convention
- Unit/Integration: `__tests__/{module}.test.ts`
- E2E: `e2e/{flow}.spec.ts`

## Domain Test Specs
- Skill 로딩/실행 테스트
- Template 치환 로직 테스트
- tRPC 라우터 프로시저별 테스트
- Drizzle 스키마 마이그레이션 테스트
- Supabase auth 흐름 테스트

## Commands
```bash
# Unit + Integration
npx vitest run

# Coverage report
npx vitest run --coverage

# E2E
npx playwright test
```

## When to Write Tests
| Situation | Required Test |
|-----------|--------------|
| 새 컴포넌트 | Unit: 렌더링, props, 이벤트 |
| 새 유틸/헬퍼 | Unit: 입출력, 엣지 케이스 |
| 새 tRPC 프로시저 | Integration: 요청/응답, 에러 처리 |
| 새 페이지 | Integration: 렌더링 + E2E: 네비게이션 |
| 버그 수정 | 재현 테스트 먼저 → 수정 → 통과 확인 |
