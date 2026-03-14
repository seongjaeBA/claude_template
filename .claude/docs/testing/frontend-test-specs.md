# Frontend Test Specs

## Component Tests (Vitest + Testing Library)

### 공통 컴포넌트
- [ ] Button: 렌더링, onClick 이벤트, disabled 상태
- [ ] Input: value 바인딩, onChange, validation 표시
- [ ] Modal: 열기/닫기, 외부 클릭 닫기
- [ ] Toast/Alert: 메시지 표시, 자동 사라짐

### 레이아웃
- [ ] Header: 네비게이션 링크, 로그인/로그아웃 상태
- [ ] Sidebar: 메뉴 아이템, 활성 상태 표시
- [ ] Footer: 링크 렌더링

## Page Tests

### 홈 페이지
- [ ] 메인 컨텐츠 렌더링
- [ ] CTA 버튼 동작
- [ ] 반응형 레이아웃

### 대시보드
- [ ] 인증 필요 (미인증 시 리다이렉트)
- [ ] 데이터 로딩 상태
- [ ] 에러 상태 표시
- [ ] 빈 상태 표시

## E2E Tests (Playwright)

### 인증 흐름
- [ ] 회원가입 → 로그인 → 대시보드 접근
- [ ] 로그아웃 → 보호된 페이지 접근 차단

### 핵심 사용자 흐름
- [ ] 홈 → 네비게이션 → 각 페이지 접근
- [ ] CRUD 전체 흐름 (생성 → 조회 → 수정 → 삭제)

### 반응형
- [ ] 모바일 뷰포트 네비게이션
- [ ] 태블릿 뷰포트 레이아웃
