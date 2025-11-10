# Gemini 에이전트 가이드

**[Base Persona]** `AgentRule/PERSONA.md`

*이 파일은 `AgentRule/PERSONA.md`에 정의된 기본 페르소나를 상속받습니다. 기본 파일의 모든 규칙이 적용되며, 아래에는 Gemini 에이전트에만 해당하는 특화 지침이 기술되어 있습니다.*

---

## Gemini 특화 지침 (Gemini-Specific Instructions)

*이 섹션에는 Gemini 에이전트 모델에만 해당하는 고유한 지침, 기능 또는 제약 사항을 기술합니다.*


이 저장소는 **Onepiece** 프로젝트입니다. 다음 문서를 참조하세요:

- **프로젝트 개요**: `AgentRule/Project/Onepiece/PROJECT_OVERVIEW.md`
  - 프로젝트 정보 (UE 5.6.1, POTENUP 최종 프로젝트)
  - 프로젝트 일정 및 평가 기준
  - 모듈 구조 (`Onepiece`, `CoffeeLibrary`, `LatteLibrary`)
  - 개발 환경 및 빌드 설정

- **코딩 컨벤션**: `AgentRule/Project/Onepiece/CODING_CONVENTIONS.md`
  - Onepiece 프로젝트 전용 규칙
  - 네트워크 모듈 컨벤션
  - `ONEPIECE_API` 매크로 사용
  - 로깅 시스템 (`PRINTLOG`, `NETWORK_LOG`)

- **Doxygen 설정**: `AgentRule/Project/Onepiece/DOXYGEN_SETUP.md`
  - 문서화 시스템 구성
  - GitHub Pages 배포 가이드

### 범용 Unreal Engine 규칙

모든 Unreal Engine 프로젝트에 공통적으로 적용되는 규칙:

- **UE 코딩 컨벤션**: `AgentRule/Project/ue_coding_conventions.md`

### 작업 시 주의사항

1. **프로젝트 컨텍스트 확인**: 작업 시작 전 `PROJECT_OVERVIEW.md`를 참조하여 프로젝트 구조 파악
2. **모듈명 사용**: `ONEPIECE_API` 매크로 사용, `LogOnepiece` 로그 카테고리 사용
3. **라이브러리 활용**: `CoffeeLibrary`(공용 유틸리티), `LatteLibrary`(게임플레이 로직) 적절히 활용
4. **문서화**: Doxygen 주석 규칙 준수