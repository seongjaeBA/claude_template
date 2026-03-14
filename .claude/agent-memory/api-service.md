# api-service Memory

## Identity
tRPC 라우터 + Supabase/Drizzle 백엔드 로직 전용 에이전트. API 설계, DB 스키마, 비즈니스 로직 담당.

## Design Decisions (확정)

### API 아키텍처
- tRPC로 type-safe RPC
- Zod input validation
- Supabase Auth 기반 인증

### DB 아키텍처
- Drizzle ORM + PostgreSQL (Supabase)
- cursor-based 페이지네이션

## Key Files
| File | Role |
|------|------|
| `src/server/trpc.ts` | tRPC 초기화 + context |
| `src/server/routers/_app.ts` | 루트 라우터 |
| `src/server/db/schema.ts` | Drizzle 스키마 |
| `src/server/db/index.ts` | DB 클라이언트 |
| `src/env.ts` | 환경변수 검증 (t3-env) |

## Pitfalls (함정)
- (아직 없음 — 작업 중 발견 시 추가)

## TODO (미구현)
- [ ] Drizzle 스키마 정의
- [ ] tRPC context + auth middleware
- [ ] 기본 CRUD 라우터
