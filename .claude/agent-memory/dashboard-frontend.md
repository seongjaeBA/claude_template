# dashboard-frontend Memory

## Identity
대시보드 페이지 전용 에이전트. 데이터 시각화, CRUD UI, 관리 기능 담당.

## Design Decisions (확정)

### 레이아웃
- Sidebar 네비게이션 + 메인 콘텐츠 영역

### 색상 시스템
| 변수 | Light | Dark |
|------|-------|------|
| `--page-bg` | `#f5f5f5` | `#0a0a0a` |
| `--page-text` | `#0a0a0a` | `#fafafa` |
| `--page-accent` | `#2563eb` | `#3b82f6` |

### Dark Mode
- 셀렉터: `class="dark"` on `<html>`
- 라이브러리: `next-themes`

## Key Files
| File | Role |
|------|------|
| `src/app/dashboard/page.tsx` | 대시보드 메인 |
| `src/app/dashboard/layout.tsx` | 대시보드 레이아웃 |
| `src/components/dashboard/` | 대시보드 전용 컴포넌트 |

## Pitfalls (함정)
- (아직 없음 — 작업 중 발견 시 추가)

## TODO (미구현)
- [ ] Sidebar 네비게이션
- [ ] 데이터 테이블 컴포넌트
- [ ] 통계 카드 컴포넌트
