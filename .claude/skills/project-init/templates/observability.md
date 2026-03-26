# Observability Setup

## LogTape vs Sentry — 용도 차이

| 기준 | LogTape | Sentry |
|------|---------|--------|
| 역할 | 구조화 로그 라이브러리 | 에러 추적 + 성능 모니터링 플랫폼 |
| 환경 | 로컬 + 서버 모두 | 주로 프로덕션 |
| 대시보드 | 없음 (stdout/파일/외부 sink) | 있음 (웹 대시보드) |
| 비용 | 무료 (라이브러리) | 프리미엄 (무료 티어 있음) |
| 설정 복잡도 | 낮음 | 중간 (DSN 설정 필요) |
| 함께 사용 | 가능 (서로 보완) | — |

---

## LogTape 설정 (구조화 로깅)

```typescript
// lib/logger.ts
import { configure, getLogger } from "@logtape/logtape";

await configure({
  sinks: {
    console: { type: "console" },
  },
  loggers: [
    { category: ["app"], sinks: ["console"], lowestLevel: "info" },
  ],
});

export const logger = getLogger(["app"]);

// 사용 예시
logger.info("User logged in", { userId: "123", method: "email" });
logger.error("DB connection failed", { error: err.message });
```

---

## Sentry 설정 (에러 추적)

### Next.js 설치
```bash
npm install @sentry/nextjs
npx @sentry/wizard@latest -i nextjs
```

### 환경변수 (`.env.local`)
```
SENTRY_DSN=https://xxx@ooo.ingest.sentry.io/yyy
NEXT_PUBLIC_SENTRY_DSN=https://xxx@ooo.ingest.sentry.io/yyy
```

### `sentry.client.config.ts`
```typescript
import * as Sentry from "@sentry/nextjs";

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: process.env.NODE_ENV === "production" ? 0.1 : 1.0,
});
```

---

## 함께 사용하는 패턴

- **LogTape**: 개발 중 구조화 로그, 서버 사이드 비즈니스 로직 추적
- **Sentry**: 프로덕션 에러 캡처, 성능 이슈 알림
- 에러 발생 시 LogTape으로 컨텍스트 로그, Sentry로 알림 발송
