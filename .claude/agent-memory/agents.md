# Agent Memory

## home-frontend
→ 별도 파일: `.claude/agent-memory/home-frontend.md`

## dashboard-frontend
→ 별도 파일: `.claude/agent-memory/dashboard-frontend.md`

## api-service
→ 별도 파일: `.claude/agent-memory/api-service.md`

## code-reviewer
- Biome 설정 기반으로 리뷰
- `"use client"` 지시어 불필요한 곳 확인 (Next.js)
- 미사용 import, 불필요한 any 타입 검출

## security-reviewer
- 환경변수 클라이언트 번들 노출 검사
- 인증/인가 우회 경로 확인
- XSS, CSRF 취약점 점검

## tdd-guide
- Vitest 패턴 사용
- 새 컴포넌트/유틸 함수 추가 시 테스트 우선
- E2E: Playwright로 핵심 사용자 흐름

## planner
- 아키텍처 변경 시 사용
- 복잡한 기능 구현 전 계획 수립

## e2e-runner
- 테스트 대상: 핵심 사용자 흐름
- 환경 설정: NEXT_PUBLIC_APP_URL, PLAYWRIGHT_BASE_URL
