# API Business Logic

## 인증/인가
- Supabase Auth로 사용자 인증
- tRPC middleware에서 세션 검증
- RLS(Row Level Security)로 DB 수준 접근 제어

## 데이터 접근 패턴
- Drizzle ORM을 통한 type-safe 쿼리
- 트랜잭션: 여러 테이블 변경 시 `db.transaction()` 사용
- 소프트 삭제: `deletedAt` 컬럼 활용 (필요 시)

## 비즈니스 규칙
- 사용자는 자신의 데이터만 CRUD 가능
- 관리자 역할은 Supabase Auth metadata로 관리
- Rate limiting: Vercel Edge Middleware 또는 upstash/ratelimit 활용
