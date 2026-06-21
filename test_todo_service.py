import pytest

import todo_service


@pytest.fixture(autouse=True)
def clean_store():
    todo_service.reset()
    yield


def test_add_todo_defaults():
    t = todo_service.add_todo("write script")
    assert t["id"] == 1
    assert t["title"] == "write script"
    assert t["priority"] == 3
    assert t["done"] is False


def test_add_todo_rejects_empty_title():
    with pytest.raises(ValueError):
        todo_service.add_todo("   ")


def test_complete_marks_done():
    t = todo_service.add_todo("record demo")
    todo_service.complete_todo(t["id"])
    assert todo_service.summary()["done"] == 1


def test_pending_excludes_completed():
    a = todo_service.add_todo("buy mic", priority=2)
    todo_service.add_todo("edit video", priority=1)
    todo_service.complete_todo(a["id"])

    pending = todo_service.get_pending()
    titles = [t["title"] for t in pending]

    # completed item must NOT appear
    assert "buy mic" not in titles
    assert titles == ["edit video"]


def test_pending_sorted_by_priority():
    todo_service.add_todo("low", priority=5)
    todo_service.add_todo("high", priority=1)
    todo_service.add_todo("mid", priority=3)

    order = [t["title"] for t in todo_service.get_pending()]
    assert order == ["high", "mid", "low"]
