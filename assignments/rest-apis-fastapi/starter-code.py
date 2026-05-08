from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Tasks API")

# TODO: Define your Task model here using Pydantic's BaseModel
# Fields: id (int), title (str), completed (bool, default False)
class Task(BaseModel):
    pass


# In-memory storage for tasks
tasks = []


# TODO: Task 1 — Create a root GET / endpoint that returns a welcome message
@app.get("/")
def root():
    pass


# TODO: Task 1 — Create a GET /health endpoint that returns {"status": "ok"}
@app.get("/health")
def health():
    pass


# TODO: Task 2 — GET /tasks — return all tasks
@app.get("/tasks")
def get_tasks():
    pass


# TODO: Task 2 — POST /tasks — add a new task from the request body
@app.post("/tasks")
def create_task(task: Task):
    pass


# TODO: Task 2 — PUT /tasks/{task_id} — update an existing task by ID
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: Task):
    pass


# TODO: Task 2 — DELETE /tasks/{task_id} — remove a task by ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    pass


# TODO: Task 3 — Add optional query parameters to GET /tasks
# completed: bool | None = None
# search: str | None = None
