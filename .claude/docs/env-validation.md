# Environment Variable Validation

## 왜 환경변수 검증이 필요한가

- 배포 시 누락된 환경변수로 인한 런타임 에러 방지
- 타입 안전성 확보 (`process.env.PORT`는 항상 `string`)
- 빌드 타임에 미리 잡기 (Vercel 배포 실패 조기 발견)

## t3-env 설정 (Zod 기반)

### 설치
```bash
npm install @t3-oss/env-nextjs zod
```

### `src/env.ts`
```typescript
import { createEnv } from "@t3-oss/env-nextjs";
import { z } from "zod";

export const env = createEnv({
  server: {
    NODE_ENV: z.enum(["development", "test", "production"]),
    DATABASE_URL: z.string().url(),
    SUPABASE_SERVICE_ROLE_KEY: z.string().min(1),
  },
  client: {
    NEXT_PUBLIC_SUPABASE_URL: z.string().url(),
    NEXT_PUBLIC_SUPABASE_ANON_KEY: z.string().min(1),
    NEXT_PUBLIC_APP_URL: z.string().url(),
  },
  runtimeEnv: {
    NODE_ENV: process.env.NODE_ENV,
    DATABASE_URL: process.env.DATABASE_URL,
    SUPABASE_SERVICE_ROLE_KEY: process.env.SUPABASE_SERVICE_ROLE_KEY,
    NEXT_PUBLIC_SUPABASE_URL: process.env.NEXT_PUBLIC_SUPABASE_URL,
    NEXT_PUBLIC_SUPABASE_ANON_KEY: process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY,
    NEXT_PUBLIC_APP_URL: process.env.NEXT_PUBLIC_APP_URL,
  },
});
```

### 사용
```typescript
import { env } from "~/env";
const dbUrl = env.DATABASE_URL; // string, 타입 안전
```

### `.env.example` (필수 커밋)
```
NODE_ENV=development
DATABASE_URL=postgresql://...
SUPABASE_SERVICE_ROLE_KEY=
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=
NEXT_PUBLIC_APP_URL=http://localhost:3000
```
