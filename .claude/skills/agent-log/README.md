---
skill: agent-log
description: 프로젝트에 Claude Code 세션 자동 로깅 시스템을 설치합니다
version: 1.0.0
author: DoppledDiggong Team
---

# Agent Log Installation Skill

이 스킬은 **Claude Code 세션의 작업 내용을 자동으로 기록**하는 시스템을 다른 프로젝트에 설치합니다.

## 설치되는 기능

- **Start Log**: 세션 시작 시 자동 생성
- **Compact Log**: 작업 중간 요약 (`/compact` 명령)
- **End Log**: 세션 종료 시 자동 생성
- **자동 훅**: 세션 시작/종료 시 자동 실행

## 설치 절차 (간편!)

### 사전 요구사항
- **Git** (사용자 정보: `git config user.name` 설정 필요)
- **Python 3.x** (시간 계산용)
- **Claude Code CLI**

### 1단계: install 폴더 복사

```bash
# 방법 1: 직접 복사
cp -r .claude/skills/agent-log/install/* /path/to/대상프로젝트/

# 방법 2: Windows 탐색기에서 드래그앤드롭
```

복사 후 구조:
```
대상프로젝트/
├── .claude/
│   ├── commands/          # /start-log, /compact, /end-log
│   └── hooks/             # 세션 시작/종료 자동 실행
└── Tools/SaveAgentQA/     # Q&A 저장 스크립트
```

### 2단계: 훅 실행 권한 (Linux/Mac)

```bash
chmod +x .claude/hooks/on-session-start.sh
chmod +x .claude/hooks/on-session-end.sh
```

### 3단계: Git 사용자 정보 확인

```bash
git config user.name   # 확인
# 없으면 설정
git config --global user.name "YourName"
```

---

**설치 완료!** Claude Code 세션마다 자동으로 작업 로그가 기록됩니다.

## 사용 방법

**자동 실행**:
- 세션 시작 → Start Log 생성
- 세션 종료 → End Log 생성

**수동 명령**:
```bash
/start-log    # Start Log 생성
/compact      # 중간 요약
/end-log      # End Log 생성
```

## 생성 로그 예시

```markdown
# dopple (251109)

# Start Log
- 20251109 19:30
- 작업자: dopple

### To Do
1. 새로운 기능 구현

## Compact Log 1
- 20251109 20:15

### 요약 내용
- 파일 A, B 수정
- 기능 X 구현 완료

### Commit 정보
**Summary (EN)**: Add feature X
**세부 내역**:
1. "기능 X" - 상세 설명

## End Log
- 20251109 22:00

### 오늘 한 일
1. 기능 X 구현
2. 테스트 완료
```

## YiSan 프로젝트 참고

원본: https://github.com/doppleddiggong/YiSan/.claude/skills/agent-log/

실제 로그 예시: `Documents/AgentLog/dopple/dopple_251109.md`

## 관련 Skill

- **commit-helper**: 커밋 메시지 자동 생성
- **docs-system**: DevLog 자동 생성

## 라이선스

MIT License
