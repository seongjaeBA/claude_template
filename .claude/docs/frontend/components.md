# Component Patterns

## Directory Structure
```
src/components/
├── ui/              # 범용 UI 컴포넌트 (Button, Input, Modal 등)
├── home/            # 홈 페이지 전용 컴포넌트
├── dashboard/       # 대시보드 전용 컴포넌트
└── layout/          # Header, Footer, Sidebar 등
```

## Naming Convention
- 파일명: `kebab-case.tsx`
- 컴포넌트: `PascalCase`
- Props: `{ComponentName}Props` 인터페이스

## Component Template
```typescript
interface ButtonProps {
  variant?: "primary" | "secondary" | "ghost";
  size?: "sm" | "md" | "lg";
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
}

export function Button({
  variant = "primary",
  size = "md",
  children,
  ...props
}: ButtonProps) {
  return <button className={cn(variants[variant], sizes[size])} {...props}>{children}</button>;
}
```

## Rules
- Server Component 기본 — `"use client"` 필요 시에만 추가
- Props drilling 3단계 이상 → Context 또는 tRPC query 사용
- 공유 컴포넌트 변경 시 관련 도메인 에이전트 병렬 리뷰 필수
