# Local Quality Checks

## 즉시 실행 명령어

```bash
npx biome check .          # 린트 + 포맷 확인
npx biome check --write .  # 린트 + 포맷 자동 수정
npx tsc --noEmit            # TypeScript 타입 검사
npx vitest run              # 단위 테스트
npx playwright test         # E2E 테스트
```

## Pre-commit 자동화 (lefthook)

`lefthook.yml`:
```yaml
pre-commit:
  commands:
    biome:
      glob: "*.{ts,tsx,js,jsx}"
      run: npx biome check --write --staged {staged_files}
```

설치:
```bash
npm install -D lefthook
npx lefthook install
```

## IDE 설정 권장

### Biome (VSCode)
- Extension: `biomejs.biome`
- `.vscode/settings.json`:
  ```json
  {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "biomejs.biome"
  }
  ```

## CI와의 관계

| 확인 단계 | 로컬 (pre-commit) | CI (Vercel) |
|-----------|-------------------|-------------|
| 린트+포맷 | 변경 파일만 (staged) | 전체 코드베이스 |
| 타입 검사 | 수동 또는 에디터 | 빌드 시 자동 |
| 테스트 | 수동 실행 | push/PR 시 자동 |
