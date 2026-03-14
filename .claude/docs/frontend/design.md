# Design System

## Color System
| Token | Light | Dark |
|-------|-------|------|
| `--bg-primary` | `#ffffff` | `#0a0a0a` |
| `--bg-secondary` | `#f5f5f5` | `#171717` |
| `--text-primary` | `#0a0a0a` | `#fafafa` |
| `--text-secondary` | `#737373` | `#a3a3a3` |
| `--accent` | `#2563eb` | `#3b82f6` |
| `--accent-hover` | `#1d4ed8` | `#60a5fa` |
| `--border` | `#e5e5e5` | `#262626` |
| `--error` | `#dc2626` | `#ef4444` |
| `--success` | `#16a34a` | `#22c55e` |

## Typography
- Font: System font stack (`-apple-system, BlinkMacSystemFont, ...`)
- Headings: `font-bold`
- Body: `font-normal`

## Spacing
- Base unit: 4px
- Scale: 4, 8, 12, 16, 24, 32, 48, 64, 96

## Breakpoints
| Name | Width |
|------|-------|
| `sm` | 640px |
| `md` | 768px |
| `lg` | 1024px |
| `xl` | 1280px |

## Dark Mode
- Selector: `class="dark"` on `<html>`
- Library: `next-themes`
- Default: system preference
