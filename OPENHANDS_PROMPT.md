# Prompt to paste into OpenHands (read on camera)

## Short version
> The latest commit on `main` broke the test suite. Run `pytest -q`, find the
> regression, fix it, and make all tests pass. Then show me a diff of what you
> changed.

## GitHub-issue version (for the Issue -> PR demo)
> Please fix the bug described in issue #1 of this repository. The pending-todo
> endpoint is returning completed items and the list is sorted in the wrong
> order. Run the tests, fix `todo_service.py`, make `pytest -q` green, then open
> a pull request that closes the issue.

## What the agent should do (so you know it worked)
1. Install deps / run `pytest -q` -> sees 2 failing tests.
2. Read `todo_service.py`, spot `get_pending()`.
3. Fix two things:
   - filter `not t["done"]` (it was returning done items)
   - sort ascending by priority (it was reversed)
4. Re-run `pytest -q` -> 5 passed.
5. (Issue->PR demo) commit + open PR.
