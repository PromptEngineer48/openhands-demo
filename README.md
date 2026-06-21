# Todo API (OpenHands demo)

Tiny Flask todo service used to demo an AI coding agent fixing a regression.

## Run

```bash
pip install -r requirements.txt
pytest -q          # run tests
python app.py      # start API on :5000
```

## Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/todos` | create a todo `{title, priority}` |
| POST | `/todos/<id>/complete` | mark done |
| GET  | `/todos/pending` | list not-done, highest priority first |
| GET  | `/summary` | counts |
