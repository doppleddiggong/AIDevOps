# Claude 에이전트 가이드

**[Base Persona]** `AgentRule/PERSONA.md`

*이 파일은 `AgentRule/PERSONA.md`에 정의된 기본 페르소나를 상속받습니다. 기본 파일의 모든 규칙이 적용되며, 아래에는 Claude 에이전트에만 해당하는 특화 지침이 기술되어 있습니다.*

---

## Claude 특화 지침 (Claude-Specific Instructions)

*이 섹션에는 Claude 에이전트 모델에만 해당하는 고유한 지침, 기능 또는 제약 사항을 기술합니다. 예를 들어, 특정 API 사용 방식이나 응답 생성 스타일을 정의할 수 있습니다.*

---

## Log 시스템 (Logging System)

**참고**: 상세한 Log 시스템 가이드는 `AgentRule/Common/Workflows/agents_log.md`를 참조하세요.

### 요약

- **Agent 시작**: `# Start Log` 기입 → 작업자 정보 → ToDo 리스트 → `[GitRoot]/AgentLog/[작업자GitID]/YYMMDD.md`에 기록
- **Agent 중간 요약**: `Compact Log` 작성 → 작업 요약 → Commit 메시지 추천
- **Agent 종료**: `End Log` 작성 → 전체 작업 요약

자세한 절차와 예시는 `AgentRule/Common/Workflows/agents_log.md`를 참조하세요.

---

## Commit 메시지 작성 (Commit Message Generation)

**참고**: 상세한 커밋 컨벤션은 `COMMIT_CONVENTION.md`를 참조하세요.

### 워크플로우

사용자가 "커밋 메시지 작성해줘!" 또는 유사한 요청을 하면, 다음 절차를 따르세요:

#### 1. Staged 파일 확인

**IMPORTANT**: 반드시 **staged 파일만** 확인합니다. 전체 diff가 아닙니다!

```bash
# Staged 파일 목록
git diff --cached --name-only

# Staged 파일의 변경 내용
git diff --cached
```

#### 2. 변경 내용 분석

Staged 파일의 변경 내용을 분석하여:
- 어떤 type인지 결정 (feat/fix/docs/style/refactor/test/chore/perf/ci/build)
- 핵심 변경 사항 파악
- 변경 이유와 목적 이해

#### 3. 커밋 메시지 생성

**형식**:
```
<type>: <subject>

<body>

<footer>
```

**규칙**:
- **Subject**: 50자 이내, 소문자 시작, 명령형, 마침표 없음
- **Body**: 72자마다 줄바꿈, 왜 변경했는지 설명 (선택사항)
- **Footer**: 이슈 참조, Breaking Changes (선택사항)

#### 4. Type 선택 가이드

| Type | 사용 시점 |
|------|-----------|
| **feat** | 새로운 기능 추가 |
| **fix** | 버그 수정 |
| **docs** | 문서만 변경 (코드 변경 없음) |
| **style** | 코드 포맷팅, 공백 등 (동작 변경 없음) |
| **refactor** | 코드 리팩토링 (기능 변경 없음) |
| **test** | 테스트 코드 추가/수정 |
| **chore** | 빌드, 설정 파일 변경 |
| **perf** | 성능 개선 |
| **ci** | CI 설정 변경 |
| **build** | 빌드 시스템 변경 |

### 예시

**사용자 요청**:
```
커밋 메시지 작성해줘!
```

**Claude 응답**:
```bash
# Staged 파일 확인 중...
git diff --cached --name-only
```

분석 결과를 바탕으로:

```
feat: add user authentication system

Implement JWT-based authentication with login and signup endpoints.
Users can now securely create accounts and manage sessions.

Includes password hashing with bcrypt and token refresh logic.
```

### 주의사항

1. **전체 diff가 아닌 staged 파일만 확인**: `git diff --cached` 사용
2. **컨텍스트 활용**: 이전 대화에서 작업한 내용을 고려
3. **명확하고 간결하게**: 불필요한 설명 제거
4. **일관된 스타일**: 프로젝트의 기존 커밋 메시지 스타일 따르기

### 자주 사용하는 표현

**사용자 요청 예시**:
- "커밋 메시지 작성해줘"
- "지금까지 작업한 내용으로 커밋 메시지 만들어줘"
- "staged 파일 보고 커밋 메시지 생성해줘"
- "커밋할 내용 정리해줘"

**모두 동일하게 처리**: staged 파일 확인 → 분석 → 커밋 메시지 생성