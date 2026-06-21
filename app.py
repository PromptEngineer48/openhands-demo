"""Tiny Flask API over todo_service."""

from flask import Flask, jsonify, request

import todo_service

app = Flask(__name__)


@app.post("/todos")
def create():
    data = request.get_json(force=True) or {}
    try:
        todo = todo_service.add_todo(data.get("title", ""), data.get("priority", 3))
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify(todo), 201


@app.post("/todos/<int:todo_id>/complete")
def complete(todo_id):
    try:
        return jsonify(todo_service.complete_todo(todo_id))
    except KeyError as exc:
        return jsonify({"error": str(exc)}), 404


@app.get("/todos/pending")
def pending():
    return jsonify(todo_service.get_pending())


@app.get("/summary")
def summary():
    return jsonify(todo_service.summary())


if __name__ == "__main__":
    app.run(port=5000, debug=True)
