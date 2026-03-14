# API Endpoints (tRPC)

## Router Structure
```
src/server/
├── trpc.ts              # tRPC 초기화 + context
├── routers/
│   ├── _app.ts          # 루트 라우터 (모든 라우터 merge)
│   ├── auth.ts          # 인증 관련 프로시저
│   └── {resource}.ts    # 리소스별 CRUD 라우터
└── db/
    ├── schema.ts        # Drizzle 스키마
    ├── index.ts         # DB 클라이언트
    └── migrations/      # 마이그레이션 파일
```

## Routing Rules
- 각 리소스별 라우터 파일 분리
- `_app.ts`에서 모든 라우터를 merge
- `protectedProcedure`: 인증 필요 프로시저
- `publicProcedure`: 인증 불필요 프로시저

## tRPC + Next.js 연동
```
src/trpc/
├── server.ts    # 서버 사이드 caller
├── client.ts    # 클라이언트 hooks
└── react.tsx    # TRPCProvider
```

## Convention
- Input validation: Zod 스키마
- 에러 처리: `TRPCError` with 적절한 code
- 페이지네이션: cursor-based (Supabase 호환)
