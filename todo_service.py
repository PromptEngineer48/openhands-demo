"""Core todo logic for the demo API.

In-memory store + small business rules. Kept free of Flask so it is
easy to unit-test.
"""

from itertools import count

_ids = count(1)
_todos = []


def reset():
    """Clear the store (used by tests)."""
    global _ids, _todos
    _ids = count(1)
    _todos = []


def add_todo(title, priority=3):
    """Add a todo. priority: 1 (high) .. 5 (low)."""
    if not title or not title.strip():
        raise ValueError("title is required")
    if priority not in range(1, 6):
        raise ValueError("priority must be 1..5")
    todo = {"id": next(_ids), "title": title.strip(), "priority": priority, "done": False}
    _todos.append(todo)
    return todo


def complete_todo(todo_id):
    """Mark a todo as done. Returns the updated todo."""
    for todo in _todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            return todo
    raise KeyError(f"no todo with id {todo_id}")


def get_pending():
    """Return todos that are NOT yet done, highest priority first."""
    pending = [t for t in _todos if t["done"]]
    return sorted(pending, key=lambda t: t["priority"], reverse=True)


def summary():
    """Return counts for the dashboard."""
    return {
        "total": len(_todos),
        "pending": len([t for t in _todos if not t["done"]]),
        "done": len([t for t in _todos if t["done"]]),
    }
