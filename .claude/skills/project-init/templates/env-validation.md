# Environment Variable Validation

## 왜 환경변수 검증이 필요한가

- 배포 시 누락된 환경변수로 인한 런타임 에러 방지
- 타입 안전성 확보 (`process.env.PORT`는 항상 `string`, 숫자가 아님)
- 빌드 타임에 미리 잡기 (Vercel 배포 실패 조기 발견)

---

## t3-env (Zod 기반, 권장)

### 설치
```bash
npm install @t3-oss/env-nextjs zod
```

### `src/env.ts`
```typescript
import { createEnv } from "@t3-oss/env-nextjs";
import { z } from "zod";

export const env = createEnv({
  // 서버 전용 환경변수 (클라이언트에 노출 안 됨)
  server: {
    NODE_ENV: z.enum(["development", "test", "production"]),
    DATABASE_URL: z.string().url().optional(),
    PORTFOLIO_PASSWORD: z.string().min(8),
  },
  // 클라이언트에서 접근 가능 (NEXT_PUBLIC_ 접두사 필요)
  client: {
    NEXT_PUBLIC_APP_URL: z.string().url(),
  },
  // 실제 process.env 매핑
  runtimeEnv: {
    NODE_ENV: process.env.NODE_ENV,
    DATABASE_URL: process.env.DATABASE_URL,
    PORTFOLIO_PASSWORD: process.env.PORTFOLIO_PASSWORD,
    NEXT_PUBLIC_APP_URL: process.env.NEXT_PUBLIC_APP_URL,
  },
});
```

### 사용 예시
```typescript
import { env } from "~/env";

// 타입 안전, 자동완성 지원
const password = env.PORTFOLIO_PASSWORD; // string
const dbUrl = env.DATABASE_URL;          // string | undefined
```

### `.env.example` (필수 커밋)
```
NODE_ENV=development
PORTFOLIO_PASSWORD=your-password-here
NEXT_PUBLIC_APP_URL=http://localhost:3000
DATABASE_URL=                             # optional
```

---

## dotenv-safe (단순 검증)

### 설치
```bash
npm install dotenv-safe
```

### 사용 (`server.ts` 또는 `next.config.ts`)
```typescript
import "dotenv-safe/config";
// .env.example에 정의된 모든 변수가 .env에 있어야 함
```

### `.env.example`
```
PORTFOLIO_PASSWORD=
NEXT_PUBLIC_APP_URL=
```

---

## 비교

| 기준 | t3-env | dotenv-safe |
|------|--------|-------------|
| 타입 안전 | ✅ (Zod) | ❌ (string만) |
| 빌드타임 검증 | ✅ | ❌ |
| 복잡도 | 중간 | 낮음 |
| Next.js 최적화 | ✅ | ❌ |
| 권장 상황 | Vercel/Next.js | 간단한 서버 앱 |
