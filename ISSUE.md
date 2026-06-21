# Bug: completed todos still show up in "pending", and order is reversed

## What happens
After I mark a todo as done, it still appears in `GET /todos/pending`.
The pending list also seems to be sorted lowest-priority first instead of
highest-priority first.

## Steps to reproduce
1. `POST /todos {"title": "buy mic", "priority": 2}`
2. `POST /todos {"title": "edit video", "priority": 1}`
3. `POST /todos/1/complete`
4. `GET /todos/pending`

## Expected
Only `"edit video"` is returned (high priority first), because `"buy mic"`
is already completed.

## Actual
`"buy mic"` is still in the list.

The test suite (`pytest -q`) is currently red:
`test_pending_excludes_completed` and `test_pending_sorted_by_priority` fail.

Started after the most recent commit on `main`.

## Acceptance
- `pytest -q` passes (all green).
- Completed todos never appear in `/todos/pending`.
- Pending list is ordered highest priority (1) first.
