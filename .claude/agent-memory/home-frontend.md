# home-frontend Memory

## Identity
홈/랜딩 페이지 전용 에이전트. UI 디자인, 컴포넌트 구현, 인터랙션 담당.

## Design Decisions (확정)

### 레이아웃
- Hero section + 주요 기능 소개 + CTA

### 색상 시스템
| 변수 | Light | Dark |
|------|-------|------|
| `--page-bg` | `#ffffff` | `#0a0a0a` |
| `--page-text` | `#0a0a0a` | `#fafafa` |
| `--page-accent` | `#2563eb` | `#3b82f6` |

### Dark Mode
- 셀렉터: `class="dark"` on `<html>`
- 라이브러리: `next-themes`

## Key Files
| File | Role |
|------|------|
| `src/app/(home)/page.tsx` | 홈 페이지 |
| `src/components/home/` | 홈 전용 컴포넌트 |

## Pitfalls (함정)
- (아직 없음 — 작업 중 발견 시 추가)

## TODO (미구현)
- [ ] Hero section 구현
- [ ] 반응형 레이아웃
