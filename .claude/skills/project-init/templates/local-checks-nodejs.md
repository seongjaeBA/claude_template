# Local Quality Checks

## 즉시 실행 명령어

```bash
npm run lint          # 린트 검사
npm run lint:fix      # 린트 자동 수정
npm run format        # 포맷 확인
npm run format:write  # 포맷 자동 적용
npm run typecheck     # TypeScript 타입 검사
npm test              # 단위 테스트
npm run test:e2e      # E2E 테스트 (Playwright)
```

## Pre-commit 자동화

### husky + lint-staged (ESLint + Prettier 조합)
커밋 시 변경된 파일에만 린트/포맷 자동 실행.
- `.husky/pre-commit` — 훅 실행 파일
- `package.json#lint-staged` — 파일 패턴별 실행 명령 정의

### lefthook 대안
`lefthook.yml` 하나로 관리. husky보다 빠름.

### Biome 단독 사용 시
```bash
biome check --write .   # 린트 + 포맷 동시 처리
```
pre-commit: `biome check --write --staged`

## IDE 설정 권장

### ESLint + Prettier
- VSCode extension: `dbaeumer.vscode-eslint` + `esbenp.prettier-vscode`
- `.vscode/settings.json`:
  ```json
  { "editor.formatOnSave": true, "editor.defaultFormatter": "esbenp.prettier-vscode" }
  ```

### Biome
- VSCode extension: `biomejs.biome`
- `.vscode/settings.json`:
  ```json
  { "editor.formatOnSave": true, "editor.defaultFormatter": "biomejs.biome" }
  ```

### oxlint
- VSCode extension: `oxc.oxc-vscode`
- Formatter는 별도 Prettier extension 병행 사용

## CI와의 관계

| 확인 단계 | 로컬 (pre-commit) | CI (GitHub Actions / Vercel) |
|-----------|-------------------|------------------------------|
| 린트       | 변경 파일만       | 전체 코드베이스              |
| 포맷       | 변경 파일만       | 전체 검사 (--check)          |
| 타입 검사  | 수동 또는 에디터  | 빌드 시 자동                 |
| 테스트     | 수동 실행         | push/PR 시 자동              |
