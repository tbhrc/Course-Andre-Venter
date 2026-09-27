# Codex Supervision Starter

Small Python project for Module 6.

## Purpose

Practise supervising a coding agent on a bounded repository task.

## Baseline

The function `summarize_tasks()` in `src/task_summary.py` is intentionally incomplete.

## Run tests

From this folder:

```bash
python -m unittest discover -s tests -v
```

The baseline should fail until the missing implementation is completed.

## Acceptance

Without changing the public function name or JSON structure:

- return total task count;
- return completed task count;
- return open task count;
- preserve task input order;
- reject malformed task objects missing `title` or `completed`.
