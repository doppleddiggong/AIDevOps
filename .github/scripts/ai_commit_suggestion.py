#!/usr/bin/env python3
"""
AI Commit Message Suggestion Generator

PR의 diff를 분석하여 프로젝트 커밋 컨벤션에 맞는 커밋 메시지를 생성합니다.
OpenAI GPT API를 사용하여 커밋 메시지를 자동 생성합니다.

Usage:
    python ai_commit_suggestion.py <pr_number> <repo_owner> <repo_name>
"""

import os
import sys
import json
from typing import Dict, List
import urllib.request
import urllib.error


def read_commit_convention() -> str:
    """프로젝트의 커밋 컨벤션 파일을 읽습니다."""
    convention_path = "AgentRule/Common/Workflows/commit_agent.md"

    try:
        with open(convention_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return """
# Commit Convention
- Conventional Commits: <type>(<scope>): <subject>
- type: feat, fix, docs, style, refactor, test, chore, perf, ci, build
- subject: 72자 이내, 한글, 마침표 없음
- body: 변경 이유, 핵심 변경사항 (100자 줄바꿈)
- footer: 관련 이슈, Breaking Change
"""


def http_request(url: str, headers: dict, data: dict = None) -> dict:
    """HTTP 요청을 보내고 JSON 응답을 반환합니다."""
    req = urllib.request.Request(url, headers=headers)

    if data:
        req.data = json.dumps(data).encode('utf-8')
        req.add_header('Content-Type', 'application/json')

    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        raise Exception(f"HTTP {e.code}: {error_body}")


def get_pr_diff(pr_number: str, repo_owner: str, repo_name: str, github_token: str) -> Dict:
    """GitHub PR의 diff와 메타데이터를 가져옵니다."""

    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # PR 정보 가져오기
    pr_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}'
    pr_data = http_request(pr_url, headers)

    # PR의 파일 변경 목록 가져오기
    files_url = f'{pr_url}/files'
    files = http_request(files_url, headers)

    # diff 조합
    diff_content = []
    file_list = []

    for file in files:
        filename = file['filename']
        file_list.append(filename)

        if 'patch' in file:
            diff_content.append(f"diff --git a/{filename} b/{filename}")
            diff_content.append(file['patch'])
            diff_content.append("")

    return {
        'title': pr_data['title'],
        'body': pr_data.get('body', ''),
        'files': file_list,
        'diff': '\n'.join(diff_content),
        'commits_count': pr_data['commits'],
        'base_branch': pr_data['base']['ref'],
        'head_branch': pr_data['head']['ref']
    }


def extract_scope_from_files(files: List[str]) -> str:
    """파일 목록에서 scope를 추출합니다."""
    # 최상위 폴더 추출
    scopes = set()
    for file_path in files:
        parts = file_path.split('/')
        if len(parts) > 1:
            # Source, Content 등의 최상위 폴더
            top_folder = parts[0]
            if top_folder not in ['.github', '.git', 'Documents', 'Tools']:
                scopes.add(top_folder)

    if not scopes:
        return "core"

    return ','.join(sorted(scopes)[:3])  # 최대 3개까지


def generate_commit_message_with_ai(pr_data: Dict, convention: str, openai_api_key: str) -> str:
    """OpenAI API를 사용하여 커밋 메시지를 생성합니다."""

    scope = extract_scope_from_files(pr_data['files'])

    # 프롬프트 구성
    prompt = f"""당신은 15년차 시니어 언리얼 엔진 개발자입니다.
아래 PR의 변경사항을 분석하여 프로젝트 커밋 컨벤션에 맞는 커밋 메시지를 생성하세요.

## 커밋 컨벤션
{convention}

## PR 정보
제목: {pr_data['title']}
설명: {pr_data['body'][:500] if pr_data['body'] else '(설명 없음)'}

## 변경된 파일 목록
{chr(10).join(pr_data['files'][:20])}

## Diff (일부)
{pr_data['diff'][:3000]}

## 요구사항
1. Conventional Commits 형식 준수: <type>(<scope>): <subject>
2. scope는 "{scope}"를 기본으로 하되, diff를 보고 더 적합한 scope가 있다면 변경 가능
3. subject는 72자 이내, 한글, 마침표 없음
4. body는 변경 이유와 핵심 변경사항을 간결하게 설명 (100자마다 줄바꿈)
5. footer에 관련 이슈나 Breaking Change 포함 (있는 경우)

출력 형식:
<type>(<scope>): <subject>

<body>

<footer>

위 형식으로만 출력하세요. 다른 설명은 불필요합니다.
"""

    # OpenAI API 호출
    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        'model': 'gpt-4o-mini',  # 비용 효율적인 모델
        'messages': [
            {
                'role': 'system',
                'content': '당신은 15년차 시니어 언리얼 엔진 개발자이며, 프로젝트의 커밋 메시지 컨벤션에 맞는 커밋 메시지를 생성하는 전문가입니다.'
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        'temperature': 0.3,
        'max_tokens': 500
    }

    result = http_request('https://api.openai.com/v1/chat/completions', headers, payload)
    commit_message = result['choices'][0]['message']['content'].strip()

    return commit_message


def main():
    """메인 실행 함수"""

    if len(sys.argv) < 4:
        print("Usage: python ai_commit_suggestion.py <pr_number> <repo_owner> <repo_name>")
        sys.exit(1)

    pr_number = sys.argv[1]
    repo_owner = sys.argv[2]
    repo_name = sys.argv[3]

    # 환경 변수에서 API 키 가져오기
    github_token = os.environ.get('GITHUB_TOKEN')
    openai_api_key = os.environ.get('OPENAI_API_KEY')

    if not github_token:
        print("Error: GITHUB_TOKEN environment variable is required", file=sys.stderr)
        sys.exit(1)

    if not openai_api_key:
        print("Error: OPENAI_API_KEY environment variable is required", file=sys.stderr)
        sys.exit(1)

    try:
        # PR diff 가져오기
        print(f"Fetching PR #{pr_number} from {repo_owner}/{repo_name}...", file=sys.stderr)
        pr_data = get_pr_diff(pr_number, repo_owner, repo_name, github_token)

        # 커밋 컨벤션 읽기
        print("Reading commit convention...", file=sys.stderr)
        convention = read_commit_convention()

        # AI로 커밋 메시지 생성
        print("Generating commit message with AI...", file=sys.stderr)
        commit_message = generate_commit_message_with_ai(pr_data, convention, openai_api_key)

        # 결과를 JSON으로 출력 (GitHub Actions에서 캡처)
        result = {
            'commit_message': commit_message,
            'pr_number': pr_number,
            'base_branch': pr_data['base_branch'],
            'head_branch': pr_data['head_branch']
        }

        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
