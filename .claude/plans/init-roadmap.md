# Initial Development Roadmap

## Phase 0: 프로젝트 초기화
**목표**: 개발 환경 세팅, 기본 프로젝트 구조 생성

### 작업 목록
- [ ] `npx create-next-app@latest` (TypeScript, App Router)
- [ ] Biome 설치 + `biome.json` 설정
- [ ] lefthook 설치 + `lefthook.yml` 설정
- [ ] t3-env 설치 + `src/env.ts` 설정
- [ ] Supabase 프로젝트 생성 + 환경변수 설정
- [ ] Drizzle ORM 설치 + 초기 스키마
- [ ] tRPC 설치 + 기본 라우터 구조
- [ ] Vitest + Playwright 설치 + 설정
- [ ] LogTape + Sentry 설치

### 완료 기준
- `npm run dev` 정상 실행
- `npx biome check .` 통과
- `npx tsc --noEmit` 통과

### 기술적 전제 조건
- Supabase 계정 + 프로젝트 생성
- Sentry 계정 + DSN 발급
- Vercel 계정 연동

---

## Phase 1: 인증 시스템
**목표**: Supabase Auth 기반 로그인/회원가입

### 작업 목록
- [ ] Supabase Auth 클라이언트 설정
- [ ] 로그인/회원가입 페이지
- [ ] Auth middleware (보호된 라우트)
- [ ] tRPC auth context

### 완료 기준
- 회원가입 → 로그인 → 대시보드 접근 E2E 통과
- 미인증 사용자 리다이렉트 동작

---

## Phase 2: 핵심 데이터 모델 + CRUD
**목표**: Drizzle 스키마 정의 + tRPC CRUD 라우터

### 작업 목록
- [ ] DB 스키마 정의 (핵심 엔티티)
- [ ] Drizzle 마이그레이션 실행
- [ ] tRPC CRUD 프로시저
- [ ] RLS 정책 설정

### 완료 기준
- CRUD 전체 흐름 Integration 테스트 통과
- 커버리지 80%+

---

## Phase 3: 프론트엔드 UI
**목표**: 홈 + 대시보드 페이지 구현

### 작업 목록
- [ ] 홈 페이지 (Hero, CTA)
- [ ] 대시보드 레이아웃 (Sidebar, Header)
- [ ] 데이터 CRUD UI
- [ ] 반응형 레이아웃

### 완료 기준
- 모든 페이지 렌더링 테스트 통과
- E2E 핵심 흐름 통과

---

## Phase 4: 관측성 + 배포
**목표**: LogTape/Sentry 연동 + Vercel 배포

### 작업 목록
- [ ] LogTape 로거 설정
- [ ] Sentry 초기화 + 에러 바운더리
- [ ] Vercel 배포 설정
- [ ] 환경변수 Vercel에 등록

### 완료 기준
- 프로덕션 빌드 성공
- Vercel 배포 정상 동작
- Sentry 대시보드에서 에러 수신 확인
