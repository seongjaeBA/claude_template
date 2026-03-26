# Test Strategy

## Test Pyramid
- **Unit**: {test_framework} — 컴포넌트, 유틸, 데이터 모델, 순수 함수
- **Integration**: 페이지 렌더링, API 호출, DB 쿼리, 미들웨어
- **E2E**: {e2e_framework} — 핵심 사용자 흐름 (인증, 메인 페이지, 네비게이션)

## Coverage Target: 80%+

## TDD Rules (필수)
1. 새 컴포넌트/기능 → **테스트 먼저 작성** (RED → GREEN → REFACTOR)
2. PR 전 `{test_command}` 통과 필수
3. 테스트 없는 새 코드 커밋 금지
4. E2E는 핵심 흐름만 유지 (과도한 E2E 지양)

## Test File Convention
- Unit/Integration: `{test_dir}/{module}.test.{ext}`
- E2E: `{e2e_dir}/{flow}.spec.{ext}`

## Domain Test Specs
{domain_test_specs}

## Commands
```bash
# Unit + Integration
{test_command}

# Coverage report
{coverage_command}

# E2E
{e2e_command}
```

## When to Write Tests
| Situation | Required Test |
|-----------|--------------|
| 새 컴포넌트 | Unit: 렌더링, props, 이벤트 |
| 새 유틸/헬퍼 | Unit: 입출력, 엣지 케이스 |
| 새 API 엔드포인트 | Integration: 요청/응답, 에러 처리 |
| 새 페이지 | Integration: 렌더링 + E2E: 네비게이션 |
| 버그 수정 | 재현 테스트 먼저 → 수정 → 통과 확인 |
