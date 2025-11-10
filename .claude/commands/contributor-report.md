---
description: 개발자별 커밋 활동 및 기여도를 분석하여 리포트를 생성합니다
---

# Contributor Analysis Report 생성

**참고**: `AgentRule/commit_contributor_analysis_agent.md`

## 실행 내용

1. Git 커밋 히스토리 분석
2. 개발자별 활동 메트릭 수집
3. 작업 패턴 및 특징 분석
4. 구조화된 기여도 리포트 작성

## 작업 지시

다음 절차를 따라 Contributor Analysis Report를 생성하세요:

### 1. 분석 대상 및 기간 확인

**대상 개발자**:
- 특정 개발자 지정: 사용자가 명시한 이름
- 전체 팀 분석: 모든 커밋 담당자

**분석 기간**:
- 기본값: 최근 3개월
- 사용자 지정 기간 가능

### 2. Git 데이터 수집

다음 명령으로 데이터를 수집합니다:

```bash
# 개발자 목록
git shortlog -sn --all --no-merges

# 특정 개발자 커밋 로그
git log --author="<name>" --no-merges --pretty=format:"%H|%ad|%s" --date=iso --numstat

# 전체 기간 통계
git log --author="<name>" --all --no-merges --shortstat
```

### 3. 파일명 및 경로 설정

**개인별 리포트**:
- 경로: `Documents/Reports/Contributors/`
- 파일명: `{개발자명}_YYYY-MM-DD.md`
- 예시: `dopple_2025-11-09.md`

**팀 전체 리포트**:
- 파일명: `TeamAnalysis_YYYY-MM-DD.md`

### 4. 리포트 구조

```markdown
# Contributor Analysis — {개발자명}

**생성 일시**: YYYY-MM-DD HH:MM KST
**분석 기간**: {StartDate} ~ {EndDate}
**이메일**: {email}
**역할**: {role}

---

## 1. 요약

- **총 커밋 수**: {totalCommits}건
- **활동 일수**: {activeDays}일 / {totalDays}일
- **평균 커밋/일**: {avgCommitsPerDay}건
- **총 코드 변경량**: +{totalAdditions} / -{totalDeletions}
- **주요 작업 영역**: {topScope}
- **기여도 순위**: {rank} / {totalContributors}

**한 줄 평가**: {oneLineAssessment}

---

## 2. 커밋 활동 메트릭

### 2.1 시간별 분포
- **가장 활발한 시간대**: {peakHours} ({peakCommitCount}건)
- **주중 평균 커밋**: {weekdayAvg}건
- **주말 평균 커밋**: {weekendAvg}건
- **활동 패턴**: {activityPattern}

### 2.2 커밋 크기 분석
- **평균 커밋 크기**: +{avgAdditions} / -{avgDeletions}
- **최대 커밋**: {largestCommitSHA} (+{maxAdditions} / -{maxDeletions})
- **커밋 크기 분포**:
  - 소형 (<50줄): {smallCount}건 ({smallPercentage}%)
  - 중형 (50-200줄): {mediumCount}건 ({mediumPercentage}%)
  - 대형 (200-500줄): {largeCount}건 ({largePercentage}%)
  - 초대형 (500줄+): {xlargeCount}건 ({xlargePercentage}%)

### 2.3 파일 변경 통계
- **평균 파일 변경 수/커밋**: {avgFilesPerCommit}개
- **총 변경 파일 수**: {totalUniqueFiles}개
- **가장 많이 수정한 파일**:
  1. {file1}: {file1Count}회
  2. {file2}: {file2Count}회
  3. {file3}: {file3Count}회

---

## 3. 작업 영역 분석

### 3.1 스코프별 분포
1. **[{scope1}]**: {scope1Count}건 ({scope1Percentage}%)
   - 설명: {scope1Description}
   - 대표 커밋: {scope1ExampleCommit}

2. **[{scope2}]**: {scope2Count}건 ({scope2Percentage}%)
3. **[{scope3}]**: {scope3Count}건 ({scope3Percentage}%)

### 3.2 타입별 분포
- **feat**: {featCount}건 ({featPercentage}%)
- **fix**: {fixCount}건 ({fixPercentage}%)
- **refactor**: {refactorCount}건 ({refactorPercentage}%)
- **docs**: {docsCount}건 ({docsPercentage}%)
- **chore**: {choreCount}건 ({chorePercentage}%)
- **test**: {testCount}건 ({testPercentage}%)

### 3.3 전문 영역
- **주요 모듈**:
  1. {module1}: {module1Percentage}%
  2. {module2}: {module2Percentage}%

- **기술 스택**:
  - C++: {cppPercentage}%
  - Python/Scripts: {pyPercentage}%
  - Documentation: {docPercentage}%

---

## 4. 커밋 품질 분석

### 4.1 커밋 메시지 품질
- **Conventional Commit 준수율**: {conventionalCommitPercentage}%
- **평균 제목 길이**: {avgTitleLength}자
- **본문 포함률**: {bodyInclusionPercentage}%
- **품질 점수**: {commitMessageQualityScore}/10

### 4.2 코드 품질 지표
- **테스트 코드 비율**: {testCodePercentage}%
- **문서화 기여**: {docContributionPercentage}%
- **리팩토링 비율**: {refactoringPercentage}%
- **버그 수정 비율**: {bugFixPercentage}%

---

## 5. 작업 패턴 및 특징

### 5.1 작업 스타일
- **커밋 빈도**: {commitFrequencyPattern}
- **작업 시간대**: {workHoursPattern}
- **작업 연속성**: {consistencyScore}/10

### 5.2 주요 기여 사항
1. **{contribution1}**
   - 일자: {date}
   - 설명: {description}

2. **{contribution2}**
   - 일자: {date}
   - 설명: {description}

---

## 6. 강점 및 개선 영역

### 6.1 강점
1. {strength1}
2. {strength2}

### 6.2 개선 제안
1. {improvement1}
2. {improvement2}

---

## 7. 다음 단계

### 권장 사항
- {recommendation1}
- {recommendation2}

---

**보고서 생성**: AI Agent (Contributor Analysis)
**다음 분석 예정**: {nextAnalysisDate}
```

### 5. 디렉토리 생성

```bash
mkdir -p Documents/Reports/Contributors
```

### 6. 메트릭 계산

**커밋 통계**:
- 총 커밋 수, 활동 일수
- 시간대별 분포
- 커밋 크기 분류

**작업 영역**:
- 스코프별, 타입별 분류
- 파일 변경 빈도

**품질 지표**:
- Conventional Commit 준수율
- 커밋 메시지 평균 길이

### 7. 주의 사항

**개인정보 보호**:
- 팀 내부용으로만 사용
- 공개 저장소에는 커밋하지 말 것
- 민감한 정보 제거 후 공유

**활용 방안**:
- 팀 회고 자료
- 성과 평가 참고
- 개인 성장 추적
- 업무 분배 참고

### 8. 사용자에게 완료 알림

```
✅ Contributor Analysis Report가 작성되었습니다.

파일: Documents/Reports/Contributors/{개발자명}_YYYY-MM-DD.md

---

**주의**: 이 리포트는 개인정보가 포함되어 있습니다.
팀 내부용으로만 사용하고, 공개 저장소에 커밋하지 마세요.
```

---

**팁**:
- 전체 팀 분석 시 개발자별 요약만 포함하여 페이지 분량 조절
- 분기별 생성하여 트렌드 분석에 활용
- 개인 성장 추적용으로 분기별 비교 리포트 작성
