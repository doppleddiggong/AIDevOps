---
description: 프로젝트 전체 상태, 진행률, 메트릭을 종합 분석한 보고서를 생성합니다
---

# Project Status Report 생성

**참고**: `AgentRule/project_report_agent.md`

## 실행 내용

1. Git 커밋 히스토리 전체 분석
2. 코드베이스 구조 및 통계 수집
3. 프로젝트 건강도 평가
4. 주요 메트릭 및 인사이트 제공

## 작업 지시

다음 절차를 따라 Project Status Report를 생성하세요:

### 1. 분석 기간 설정

**기본값**: 프로젝트 시작부터 현재까지
**사용자 지정**: 특정 기간 (예: 최근 6개월)

### 2. 데이터 수집

#### 2.1 Git 데이터
```bash
# 전체 커밋 통계
git log --all --no-merges --pretty=format:"%H|%an|%ae|%ad|%s" --date=iso
git log --all --no-merges --numstat --pretty=format:"%H"
git shortlog -sn --all --no-merges

# 최초/최근 커밋
git log --all --reverse --pretty=format:"%H|%ad" --date=iso | head -1
git log --all --pretty=format:"%H|%ad" --date=iso | head -1
```

#### 2.2 코드베이스 분석
```bash
# 파일/라인 수 (cloc 사용 권장)
find Source -type f \( -name "*.cpp" -o -name "*.h" \) | wc -l

# 언어별 분포
cloc Source Plugins --json
```

### 3. 파일명 및 경로 설정

**경로**: `Documents/Reports/`
**파일명**: `ProjectReport_YYYY-MM-DD.md`
**최신 링크**: `LatestReport.md` (선택)

### 4. 리포트 구조

```markdown
# Project Report — {프로젝트명}

**생성 일시**: YYYY-MM-DD HH:MM KST
**보고 기간**: {StartDate} ~ {EndDate}
**프로젝트 버전**: {ProjectVersion}
**엔진 버전**: {EngineVersion}

---

## 1. 전체 요약

- **프로젝트 상태**: {Active/OnTrack/AtRisk/Completed}
- **전체 진행률**: {ProgressPercentage}%
- **총 커밋 수**: {totalCommits}건
- **활동 기간**: {activeDays}일
- **참여 개발자**: {contributorCount}명
- **주요 성과**: {topAchievements}

**한 줄 요약**: {oneLineSummary}

---

## 2. 프로젝트 메트릭

### 2.1 코드베이스 현황
- **총 파일 수**: {totalFiles}개
- **총 코드 라인 수**: {totalLOC}줄
- **언어별 분포**:
  - C++: {cppPercentage}% ({cppLOC}줄)
  - Python: {pyPercentage}% ({pyLOC}줄)
  - Markdown: {mdPercentage}% ({mdLOC}줄)

### 2.2 커밋 통계
- **총 커밋 수**: {totalCommits}건
- **일 평균 커밋**: {avgCommitsPerDay}건
- **주 평균 커밋**: {avgCommitsPerWeek}건
- **월 평균 커밋**: {avgCommitsPerMonth}건
- **최초 커밋**: {firstCommitDate} ({firstCommitSHA})
- **최근 커밋**: {latestCommitDate} ({latestCommitSHA})

### 2.3 타입별 커밋 분포
- **feat**: {featCount}건 ({featPercentage}%)
- **fix**: {fixCount}건 ({fixPercentage}%)
- **refactor**: {refactorCount}건 ({refactorPercentage}%)
- **docs**: {docsCount}건 ({docsPercentage}%)
- **chore**: {choreCount}건 ({chorePercentage}%)

### 2.4 스코프별 활동 (상위 5개)
1. **[{scope1}]**: {scope1Count}건 ({scope1Percentage}%)
2. **[{scope2}]**: {scope2Count}건 ({scope2Percentage}%)
3. **[{scope3}]**: {scope3Count}건 ({scope3Percentage}%)
4. **[{scope4}]**: {scope4Count}건 ({scope4Percentage}%)
5. **[{scope5}]**: {scope5Count}건 ({scope5Percentage}%)

---

## 3. 모듈별 현황

**주의**: 프로젝트 구조에 맞게 커스터마이징 필요

### 3.1 [모듈명 1]
- **파일 수**: {files}개
- **코드 라인 수**: {loc}줄
- **최근 변경**: {recentChanges}
- **주요 기능**:
  - {feature1}
  - {feature2}
- **상태**: {status}

### 3.2 [모듈명 2]
- **파일 수**: {files}개
- **코드 라인 수**: {loc}줄
...

---

## 4. 주요 성과 및 마일스톤

### 4.1 완료된 주요 기능
1. **{Feature1}**
   - 완료 일자: {date}
   - 설명: {description}
   - 관련 커밋: {commits}

2. **{Feature2}**
   - 완료 일자: {date}
   - 설명: {description}

### 4.2 주요 버그 수정
1. **{BugFix1}** ({date})
2. **{BugFix2}** ({date})

### 4.3 성능 개선
1. **{PerfImprovement1}** ({date})

---

## 5. 문서화 현황

### 5.1 코드 문서화
- **Doxygen 문서**: {doxygenStatus}
  - 경로: {doxygenUrl}
  - 마지막 업데이트: {doxygenLastUpdate}
- **문서화율**: {docCoveragePercentage}%

### 5.2 프로젝트 문서
- **README.md**: {readmeStatus}
- **DevLog**: {devLogCount}개 (일일), {monthlyLogCount}개 (월간)
- **기타 문서**: {otherDocsCount}개

---

## 6. 기술 부채 및 리스크

### 6.1 식별된 기술 부채
1. **{TechDebt1}**
   - 설명: {description}
   - 영향도: {impact}
   - 우선순위: {priority}
   - 예상 해결 시간: {estimatedTime}

### 6.2 리스크 평가
1. **{Risk1}**
   - 확률: {probability}
   - 영향: {impact}
   - 완화책: {mitigation}

---

## 7. 품질 지표

### 7.1 코드 품질
- **컨벤션 준수율**: {conventionAdherencePercentage}%
- **주석 비율**: {commentRatioPercentage}%
- **평균 함수 길이**: {avgFunctionLength}줄

### 7.2 커밋 품질
- **Conventional Commit 준수율**: {conventionalCommitPercentage}%
- **평균 커밋 크기**: +{avgAdditions} / -{avgDeletions}
- **커밋 메시지 품질 점수**: {commitMessageQualityScore}/10

---

## 8. 팀 협업 현황

### 8.1 개발자별 기여도 (상위 5명)
1. {contributor1}: {commits1}건 ({percentage1}%)
2. {contributor2}: {commits2}건 ({percentage2}%)
3. {contributor3}: {commits3}건 ({percentage3}%)
4. {contributor4}: {commits4}건 ({percentage4}%)
5. {contributor5}: {commits5}건 ({percentage5}%)

### 8.2 협업 패턴
- **코드 리뷰 활동**: {codeReviewCount}건
- **이슈 해결**: {resolvedIssues}건 / {totalIssues}건

---

## 9. 미해결 사항

### 9.1 TODO 목록
- [ ] {TODO1} (출처: {source}, 우선순위: {priority})
- [ ] {TODO2} (출처: {source}, 우선순위: {priority})

### 9.2 진행 중인 작업
- {InProgressTask1} (담당: {assignee}, 진행률: {progress}%)

---

## 10. 다음 단계 및 권장사항

### 10.1 단기 목표 (1-4주)
1. {ShortTermGoal1}
   - 근거: {rationale}
   - 예상 효과: {expectedOutcome}

### 10.2 중기 목표 (1-3개월)
1. {MidTermGoal1}
   - 근거: {rationale}
   - 예상 효과: {expectedOutcome}

### 10.3 장기 목표 (3개월+)
1. {LongTermGoal1}
   - 근거: {rationale}
   - 예상 효과: {expectedOutcome}

---

## 11. 결론

{conclusionSummary}

---

**보고서 생성**: AI Agent (Project Report Agent)
**다음 보고서 예정일**: {nextReportDate}
```

### 5. 디렉토리 생성

```bash
mkdir -p Documents/Reports
```

### 6. 프로젝트 상태 판단

다음 기준으로 프로젝트 상태를 평가합니다:

- **Active**: 최근 7일 내 커밋 있음
- **OnTrack**: 진행률 순조로움, 리스크 낮음
- **AtRisk**: 리스크 높음, 차단 요인 존재
- **Completed**: 프로젝트 종료

### 7. 모듈별 커스터마이징

**중요**: 프로젝트 구조에 맞게 모듈 섹션을 수정해야 합니다.

예시 (Unreal Engine 프로젝트):
- Source/ProjectName/
- Source/Library1/
- Source/Library2/
- Plugins/Plugin1/

예시 (Web 프로젝트):
- src/components/
- src/services/
- src/utils/

### 8. 사용자에게 완료 알림

```
✅ Project Status Report가 작성되었습니다.

파일: Documents/Reports/ProjectReport_YYYY-MM-DD.md

---

**참고사항**:
- 모듈별 현황은 프로젝트 구조에 맞게 커스터마이징하세요
- 주기적으로 생성하여 프로젝트 트렌드 분석에 활용하세요
- 이해관계자 보고용으로 적합합니다
```

---

**팁**:
- 분기별 또는 마일스톤 완료 시 생성
- DevLog, Monthly Log 데이터 참조
- 주요 메트릭 추이를 시각화 (Mermaid 차트)
- 프로젝트 상태를 객관적 데이터로 평가
