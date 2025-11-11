# GitHub Actions Workflows

이 디렉토리에는 프로젝트의 자동화된 워크플로우들이 포함되어 있습니다.

## 📋 워크플로우 목록

### 🤖 AI Commit Message Suggestion

**파일**: `ai-commit-suggestion.yml`, `apply-commit-suggestion.yml`

PR 생성 시 AI가 프로젝트 커밋 컨벤션에 맞는 커밋 메시지를 자동으로 제안합니다.

#### 동작 방식
```
PR 생성 → Diff 분석 → OpenAI API 호출 → 커밋 메시지 제안 → PR 코멘트 등록
```

#### 사용 방법

**1. 자동 제안 (PR 생성 시)**
- PR을 생성하면 자동으로 AI 제안 코멘트가 등록됩니다
- Draft PR은 제외됩니다

**2. 제안 적용**

Option A: 수동 적용 (권장)
```bash
git checkout <pr-branch>
git commit --amend
# 에디터에서 AI 제안 메시지로 교체
git push --force-with-lease
```

Option B: 자동 적용
- PR 코멘트의 링크 클릭
- Actions 탭에서 "Run workflow"
- PR 번호 입력 후 실행

#### 설정
- **API Key**: `OPENAI_API_KEY` (Secrets에 설정됨)
- **모델**: GPT-4o-mini
- **컨벤션**: `AgentRule/Common/Workflows/commit_agent.md` 참조

---

### 📊 DevLog 생성

**파일**: `daily-report.yml`, `weekly-report.yml`

일일/주간 개발 로그를 자동으로 생성합니다.

#### 트리거
- **Daily**: 매일 KST 09:00 (cron)
- **Weekly**: 매주 일요일 KST 21:00 (cron)
- 수동 실행 가능 (`workflow_dispatch`)

#### 출력
- `Documents/DevLog/Daily/YYYY-MM-DD.md`
- `Documents/DevLog/Weekly/YYYY-WW.md`

---

### 📚 문서 배포

**파일**: `honkit.yml`, `doxygen.yml`

프로젝트 문서를 자동으로 빌드하고 GitHub Pages에 배포합니다.

#### HonKit
- DevLog 및 가이드 문서를 웹 페이지로 변환
- 배포: `https://<username>.github.io/<repo>/`

#### Doxygen
- 코드 API 문서 자동 생성
- C++/언리얼 엔진 코드 문서화

---

## 🔧 문제 해결

### AI 제안이 동작하지 않는 경우

1. **GitHub Secrets 확인**
   - Settings > Secrets and variables > Actions
   - `OPENAI_API_KEY` 확인

2. **권한 확인**
   - `pull-requests: write`
   - `contents: write`

3. **Draft PR 확인**
   - Draft PR은 트리거되지 않습니다
   - "Ready for review"로 변경

### DevLog가 생성되지 않는 경우

1. **커밋 확인**
   - 해당 날짜에 커밋이 있는지 확인
   - `docs` 브랜치에 push되었는지 확인

2. **Actions 로그 확인**
   - Actions 탭에서 실패 로그 확인

---

## 📂 관련 파일

```
.github/
├── workflows/              # 워크플로우 정의
│   ├── ai-commit-suggestion.yml
│   ├── apply-commit-suggestion.yml
│   ├── daily-report.yml
│   ├── weekly-report.yml
│   ├── honkit.yml
│   └── doxygen.yml
├── scripts/                # 워크플로우 스크립트
│   ├── ai_commit_suggestion.py
│   ├── devlog/
│   │   ├── generate_daily.py
│   │   ├── generate_weekly.py
│   │   └── generate_gpt_feedback.py
│   └── generate_summary.py
└── config.yml              # 워크플로우 설정
```

---

## 🔗 관련 문서

- [Commit Convention](../../AgentRule/Common/Workflows/commit_agent.md)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
