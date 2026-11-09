#!/usr/bin/env python3
"""
Velocity & Progress Tracker for 'The Journey'
Parses PROGRESS.md to generate statistics, velocity metrics, and completion summaries.

Usage:
    python tools/tracker.py           # print the dashboard
    python tools/tracker.py --write   # also refresh the Summary Dashboard in PROGRESS.md
"""

import os
import re
import sys
from datetime import datetime

# Windows consoles often default to cp1252, which cannot print emoji.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

DATE_FORMAT = "%Y-%m-%d"

PROGRESS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "PROGRESS.md")

def parse_progress():
    if not os.path.exists(PROGRESS_FILE):
        print(f"Error: Could not find {PROGRESS_FILE}")
        sys.exit(1)

    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    tasks = []
    # Match markdown table rows: | `ID` | Title | Status | Start Date | PR Opened | Merged | Hours | Difficulty | PR Link | Mentor Notes |
    row_pattern = re.compile(r'\|\s*`([^`]+)`\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|')
    
    for line in content.splitlines():
        match = row_pattern.match(line.strip())
        if match:
            task_id = match.group(1).strip()
            title = match.group(2).strip()
            status = match.group(3).strip()
            start_date = match.group(4).strip()
            pr_opened = match.group(5).strip()
            merged = match.group(6).strip()
            hours_str = match.group(7).strip()
            diff_str = match.group(8).strip()
            pr_link = match.group(9).strip()
            notes = match.group(10).strip()

            hours = 0.0
            if hours_str and hours_str != "-":
                try:
                    hours = float(hours_str.replace("h", "").replace("hrs", "").strip())
                except ValueError:
                    pass

            diff = None
            if diff_str and diff_str != "-":
                try:
                    diff = int(diff_str.strip())
                except ValueError:
                    pass

            tasks.append({
                "id": task_id,
                "title": title,
                "status": status,
                "start_date": start_date,
                "pr_opened": pr_opened,
                "merged": merged,
                "hours": hours,
                "difficulty": diff,
                "notes": notes
            })

    return tasks

def parse_date(value):
    try:
        return datetime.strptime(value.strip(), DATE_FORMAT).date()
    except ValueError:
        return None


def cycle_days(task):
    """Days from start date to merge; a same-day merge counts as 1 day."""
    start, merged = parse_date(task["start_date"]), parse_date(task["merged"])
    if start is None or merged is None:
        return None
    return max((merged - start).days, 1)


def calculate_stats(tasks):
    total = len(tasks)
    if total == 0:
        return {}

    completed = sum(1 for t in tasks if "Mastered" in t["status"] or "🟢" in t["status"])
    in_progress = sum(1 for t in tasks if "In Progress" in t["status"] or "🟡" in t["status"])
    in_review = sum(1 for t in tasks if "In Review" in t["status"] or "🔵" in t["status"])
    not_started = sum(1 for t in tasks if "Not Started" in t["status"] or "⚪" in t["status"])

    total_hours = sum(t["hours"] for t in tasks)
    completed_hours = sum(t["hours"] for t in tasks if "Mastered" in t["status"] or "🟢" in t["status"])

    diffs = [t["difficulty"] for t in tasks if t["difficulty"] is not None]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0.0

    cycles = [c for c in (cycle_days(t) for t in tasks) if c is not None]
    avg_cycle = sum(cycles) / len(cycles) if cycles else None

    percent = (completed / total) * 100 if total > 0 else 0.0
    avg_hours_per_done = completed_hours / completed if completed > 0 else 0.0

    return {
        "total": total,
        "completed": completed,
        "in_progress": in_progress,
        "in_review": in_review,
        "not_started": not_started,
        "percent": percent,
        "total_hours": total_hours,
        "avg_hours_per_done": avg_hours_per_done,
        "avg_diff": avg_diff,
        "avg_cycle": avg_cycle,
    }

def print_dashboard(stats):
    print("=" * 64)
    print(" 🚀 THE JOURNEY - VELOCITY & PROGRESS DASHBOARD ")
    print("=" * 64)
    print(f" Total Milestones & Exercises : {stats['total']}")
    print(f" 🟢 Mastered (Completed)     : {stats['completed']} ({stats['percent']:.1f}%)")
    print(f" 🔵 In Review (PR Open)      : {stats['in_review']}")
    print(f" 🟡 In Progress               : {stats['in_progress']}")
    print(f" ⚪ Not Started              : {stats['not_started']}")
    print("-" * 64)
    print(f" ⏱️ Total Hours Logged        : {stats['total_hours']:.1f} hrs")
    if stats['completed'] > 0:
        print(f" ⚡ Avg Hours per Mastered    : {stats['avg_hours_per_done']:.1f} hrs")
    if stats['avg_cycle'] is not None:
        print(f" 📅 Avg Cycle Time            : {stats['avg_cycle']:.1f} days")
    if stats['avg_diff'] > 0:
        print(f" 🎯 Avg Difficulty Rating    : {stats['avg_diff']:.1f} / 5.0")
    print("=" * 64)

def write_summary(stats, tasks):
    """Rewrite the Summary Dashboard bullet values in PROGRESS.md."""
    with open(PROGRESS_FILE, "r", encoding="utf-8", newline="") as f:
        content = f.read()

    cycle = f"{stats['avg_cycle']:.1f} days" if stats["avg_cycle"] is not None else "- days"
    milestones = sum(1 for t in tasks if t["id"].startswith("M-"))
    exercises = len(tasks) - milestones
    replacements = {
        r"(\* \*\*Total Tasks\*\*: )[^\r\n]*": rf"\g<1>{len(tasks)} ({exercises} Exercises + {milestones} Milestones)",
        r"(\* \*\*Completed\*\*: )[^\r\n]*": rf"\g<1>{stats['completed']} / {stats['total']} ({stats['percent']:.1f}%)",
        r"(\* \*\*Total Hours Logged\*\*: )[^\r\n]*": rf"\g<1>{stats['total_hours']:.1f} hrs",
        r"(\* \*\*Average Cycle Time\*\*: )[^\r\n]*": rf"\g<1>{cycle}",
    }
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content, count=1)

    with open(PROGRESS_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    print(f" ✍️  Summary Dashboard updated in {os.path.basename(PROGRESS_FILE)}")


if __name__ == "__main__":
    tasks = parse_progress()
    stats = calculate_stats(tasks)
    if not stats:
        print("No tasks found in PROGRESS.md")
        sys.exit(1)
    print_dashboard(stats)
    if "--write" in sys.argv[1:]:
        write_summary(stats, tasks)
