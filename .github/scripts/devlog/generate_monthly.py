#!/usr/bin/env python3
"""Monthly DevLog Generator - 월간 커밋 활동 분석"""
import os, sys, subprocess
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import re

def run_git(args):
    try:
        result = subprocess.run(["git"] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='replace')
        return result.stdout if result.returncode == 0 else ""
    except:
        return ""

def get_commits_for_month(year, month):
    first_day = datetime(year, month, 1)
    last_day = datetime(year, month + 1, 1) - timedelta(seconds=1) if month < 12 else datetime(year + 1, 1, 1) - timedelta(seconds=1)
    
    log = run_git(["log", "--all", "--no-merges", f"--since={first_day:%Y-%m-%d}", f"--until={last_day:%Y-%m-%d}", "--pretty=format:%H|%an|%ad|%s", "--date=iso"])
    
    commits = []
    for line in log.strip().split('\n'):
        if line:
            parts = line.split('|', 3)
            if len(parts) >= 4:
                commits.append({'hash': parts[0][:7], 'author': parts[1], 'date': parts[2][:10], 'subject': parts[3]})
    return commits

def parse_commit(subject):
    m = re.match(r'^(\w+)(?:\(([^)]+)\))?: (.+)$', subject)
    return {'type': m.group(1), 'scope': m.group(2) or '', 'desc': m.group(3)} if m else {'type': 'other', 'scope': '', 'desc': subject}

def generate_monthly_report(year, month, output_path):
    print(f"Generating monthly report for {year}-{month:02d}...")
    commits = get_commits_for_month(year, month)
    
    if not commits:
        print(f"No commits found")
        return False
    
    parsed = [parse_commit(c['subject']) for c in commits]
    types = Counter(p['type'] for p in parsed)
    scopes = Counter(p['scope'] for p in parsed if p['scope'])
    contributors = Counter(c['author'] for c in commits)
    active_days = len(set(c['date'] for c in commits))
    
    # Weekly grouping
    weeks = defaultdict(list)
    for c in commits:
        week_num = (int(c['date'][8:10]) - 1) // 7 + 1
        weeks[week_num].append(c)
    
    # Build report
    lines = [
        f"# Monthly DevLog — {year}-{month:02d}",
        "", "## 개요",
        f"- **총 커밋 수**: {len(commits)}건",
        f"- **활동 일수**: {active_days}일",
        f"- **참여 개발자**: {len(contributors)}명",
        ""
    ]
    
    if scopes:
        top_scopes = ', '.join([f"{s} ({c}건)" for s, c in scopes.most_common(3)])
        lines.append(f"- **주요 스코프**: {top_scopes}")
        lines.append("")
    
    lines.append("## 주간별 진행 현황")
    lines.append("")
    for week_num in sorted(weeks.keys()):
        week_commits = weeks[week_num]
        lines.append(f"### Week {week_num}")
        lines.append(f"- **커밋 수**: {len(week_commits)}건")
        lines.append("- **주요 작업**:")
        for c in week_commits[:5]:
            p = parse_commit(c['subject'])
            scope_str = f"[{p['scope']}] " if p['scope'] else ""
            lines.append(f"  - {scope_str}{p['desc'][:60]} ({c['hash']})")
        lines.append("")
    
    lines.append("## 타입별 분석")
    total = len(commits)
    for t, cnt in sorted(types.items(), key=lambda x: x[1], reverse=True):
        pct = cnt / total * 100
        lines.append(f"- **{t}**: {cnt}건 ({pct:.1f}%)")
    lines.append("")
    
    if scopes:
        lines.append("## 스코프별 분석")
        for s, cnt in sorted(scopes.items(), key=lambda x: x[1], reverse=True)[:5]:
            pct = cnt / total * 100
            lines.append(f"- **[{s}]**: {cnt}건 ({pct:.1f}%)")
        lines.append("")
    
    lines.append("## 기여자")
    for author, cnt in sorted(contributors.items(), key=lambda x: x[1], reverse=True):
        pct = cnt / total * 100
        lines.append(f"- **{author}**: {cnt}건 ({pct:.1f}%)")
    
    lines.append("")
    lines.append("---")
    lines.append(f"**생성 일시**: {datetime.now():%Y-%m-%d %H:%M KST}")
    
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"✅ Monthly report: {output_path}")
    return True

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Generate monthly DevLog')
    parser.add_argument('--year', type=int, default=datetime.now().year)
    parser.add_argument('--month', type=int, default=(datetime.now().month - 1) or 12)
    parser.add_argument('--out', type=str, help='Output file path')
    args = parser.parse_args()
    
    year, month = args.year, args.month
    if month == 0:
        month, year = 12, year - 1
    
    out = args.out or f"Documents/DevLog/Monthly/{year}-{month:02d}.md"
    sys.exit(0 if generate_monthly_report(year, month, out) else 1)
