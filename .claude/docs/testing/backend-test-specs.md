# Backend Test Specs

## tRPC Router Tests

### 인증 라우터
- [ ] 로그인 프로시저: 올바른 자격증명 → 세션 반환
- [ ] 로그인 프로시저: 잘못된 자격증명 → 에러
- [ ] 회원가입 프로시저: 새 사용자 생성
- [ ] 회원가입 프로시저: 중복 이메일 → 에러

### 데이터 CRUD 라우터
- [ ] list: 페이지네이션 동작
- [ ] get: 존재하는 ID → 데이터 반환
- [ ] get: 존재하지 않는 ID → 404 에러
- [ ] create: 유효한 입력 → 생성 성공
- [ ] create: 유효하지 않은 입력 → validation 에러
- [ ] update: 소유자만 수정 가능
- [ ] delete: 소유자만 삭제 가능

## Drizzle ORM Tests

### 스키마
- [ ] 마이그레이션 적용 성공
- [ ] 외래키 제약조건 검증

### 쿼리
- [ ] 기본 CRUD 쿼리 동작
- [ ] 복잡한 조인 쿼리
- [ ] 트랜잭션 롤백

## Supabase Integration

### Auth
- [ ] Supabase Auth 세션 검증
- [ ] RLS(Row Level Security) 정책 동작

### Storage
- [ ] 파일 업로드/다운로드
- [ ] 버킷 접근 권한
