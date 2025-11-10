# Onepiece 프로젝트 개발 문서

이 사이트는 언리얼 엔진 5.6.1과 C++로 개발 중인 **Onepiece 프로젝트** (POTENUP 최종 프로젝트)의 모든 기술 문서, 기획 자료, 개발 로그를 통합 관리하는 공간입니다.

---

## 📂 문서 구조

### 1. 📚 API 문서 (Doxygen)
C++ 소스 코드의 주석을 기반으로 자동 생성되는 API 레퍼런스입니다. 클래스, 함수, 변수 등 코드 레벨의 상세한 정보를 확인할 수 있습니다.

- **[API 문서 바로가기 &raquo;](https://doppleddiggong.github.io/Onepiece/doxygen/)**

### 2. 📝 시스템 설계 및 기획 (Planning)
주요 시스템의 아키텍처 설계, 기능 명세, 기술 연구(R&D) 등 프로젝트의 기획 및 설계와 관련된 모든 문서를 포함합니다.

- **프로젝트 단계:**
  - **기획 단계** (2025.11.18): 프로젝트 구체화 및 핵심 기능 설계
  - **프로토 단계** (2025.12.09): 핵심 기능 최소 1개 이상 실체 구현
  - **알파 단계** (2025.12.22): 각 기능들의 실체 연동
  - **베타 단계** (2026.01.05): 기술적 완성도 평가
  - **최종 발표** (2026.01.08): 기업 초청 평가

### 3. 📅 개발 로그 (DevLog)
GitHub Actions를 통해 매일 자동으로 생성되는 개발 일지입니다. 커밋 내역, 코드 변경 사항 등 일일 개발 활동이 투명하게 기록됩니다.

- **주요 기능:**
  - **Daily Log:** 매일 오전 9시(KST)에 자동으로 생성되는 일일 개발 로그
  - **Weekly Summary:** 매주 일요일 밤에 생성되는 주간 요약 리포트
  - **[자동화 가이드 &raquo;](DevLog/WORKFLOW_GUIDE.md)**: 개발 로그를 포함한 전체 자동화 워크플로우 상세 가이드

### 4. 📖 가이드 (Guide)
프로젝트 관련 가이드, 평가 기준, 참고 자료 등을 보관합니다.

- **POTENUP 프로젝트 평가**: 단계별 평가 기준 및 일정

### 5. 🎮 마스터 데이터 (MasterData)
게임 데이터, 설정 파일, 테이블 등을 관리합니다.

### 6. ⚙️ 환경 설정 (Preference)
개발 환경 설정, 툴 설정 등을 기록합니다.

---

## 🏗️ 프로젝트 정보

- **엔진**: Unreal Engine 5.6.1
- **언어**: C++20, Blueprint
- **모듈**:
  - `Onepiece` (메인 게임 모듈)
  - `CoffeeLibrary` (공용 유틸리티)
  - `LatteLibrary` (게임플레이 로직)
- **개발 툴**: JetBrains Rider, Visual Studio, Doxygen, Git LFS

---

## 🔗 관련 링크

- **GitHub Repository**: [doppleddiggong/Onepiece](https://github.com/doppleddiggong/Onepiece)
- **프로젝트 개요**: [PROJECT_OVERVIEW.md](../AgentRule/Project/Onepiece/PROJECT_OVERVIEW.md)
- **코딩 컨벤션**: [CODING_CONVENTIONS.md](../AgentRule/Project/Onepiece/CODING_CONVENTIONS.md)

---

**프로젝트 시작일**: 2025-11-10
**문서 업데이트일**: 2025-11-10
