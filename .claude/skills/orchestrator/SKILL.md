---
name: orchestrator
description: Global .agent-hub의 기술들을 각 플랫폼(.claude, .gemini)으로 동기화하고 환경을 초기화합니다. 새로운 기술 추가 시나 환경 설정이 어긋났을 때 실행합니다.
---

# Orchestrator: 에이전트 환경 동기화 지침

너는 이 기술을 사용하여 `.agent-hub`에 저장된 모든 기술을 Claude와 Gemini CLI 환경에 결합한다.

## 수행 절차

1.  **자산 확인**: `../assets/config.json` 파일을 읽어 플랫폼별 타겟 경로와 동기화 옵션을 확인하라.
2.  **로직 실행**: `../scripts/init_orchestrator.py` 스크립트를 실행하여 다음 작업을 수행하라.
    - `.agent-hub/skills` 내부의 각 기술 폴더를 타겟 경로에 심볼릭 링크로 연결.
    - Claude의 `settings.json` 등에 커스텀 기술 경로가 등록되어 있는지 확인 및 수정.
3.  **결과 보고**: 심볼릭 링크가 생성된 목록을 사용자에게 요약하여 보고하고, 플랫폼 설정 파일이 변경된 경우 그 내용을 알린다.

## 주의 사항
- 절대 파일을 복사(Copy)하지 마라. 반드시 심볼릭 링크(Symbolic Link)를 사용하여 원본 소스가 하나로 유지되게 하라(Single Source of Truth, SSOT).
- 권한 에러 발생 시 사용자에게 관리자 권한(sudo 또는 관리자 터미널) 실행을 요청하라.