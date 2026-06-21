#!/usr/bin/env bash
# Builds the demo git history: a clean working commit, then a "bad" commit
# that introduces the regression. Run once from inside openhands-demo/.
set -e

git init -q
git add .
git commit -q -m "Working todo API with passing tests"

# Introduce the regression into get_pending():
#  - returns DONE items instead of pending
#  - sorts in reverse (lowest priority first)
python - <<'PY'
import re, pathlib
p = pathlib.Path("todo_service.py")
s = p.read_text()
s = s.replace('pending = [t for t in _todos if not t["done"]]',
              'pending = [t for t in _todos if t["done"]]')
s = s.replace('return sorted(pending, key=lambda t: t["priority"])',
              'return sorted(pending, key=lambda t: t["priority"], reverse=True)')
p.write_text(s)
PY

git add todo_service.py
git commit -q -m "Refactor get_pending filtering and ordering"

echo "Done. HEAD = bad commit, HEAD~1 = working version."
echo "Run 'pytest -q' to see 2 failing tests."
