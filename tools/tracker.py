#!/usr/bin/env python3
"""
Velocity & Progress Tracker for 'The Journey'
Parses PROGRESS.md to generate statistics, velocity metrics, and completion summaries.
"""

import os
import re
import sys
from datetime import datetime

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
                "merged": merged,
                "hours": hours,
                "difficulty": diff,
                "notes": notes
            })

    return tasks

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
        "avg_diff": avg_diff
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
    if stats['avg_diff'] > 0:
        print(f" 🎯 Avg Difficulty Rating    : {stats['avg_diff']:.1f} / 5.0")
    print("=" * 64)

if __name__ == "__main__":
    tasks = parse_progress()
    stats = calculate_stats(tasks)
    print_dashboard(stats)
