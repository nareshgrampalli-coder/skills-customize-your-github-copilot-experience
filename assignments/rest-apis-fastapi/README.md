# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework in Python, learning how to define routes, handle path and query parameters, validate request bodies, and return structured JSON responses.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application and define your first API endpoint. Run the development server and verify the API responds correctly using the auto-generated interactive docs.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Define a `GET /` root endpoint that returns a JSON welcome message, e.g. `{"message": "Welcome to my API"}`
- Define a `GET /health` endpoint that returns `{"status": "ok"}`
- Be runnable with `uvicorn main:app --reload`


### 🛠️ Build CRUD Endpoints for a Resource

#### Description
Create a simple in-memory "tasks" API that supports Create, Read, Update, and Delete operations. Use a Python list or dictionary to store tasks while the server is running.

#### Requirements
Completed program should:

- Define a `Task` model using Pydantic's `BaseModel` with fields: `id` (int), `title` (str), and `completed` (bool, default `False`)
- Implement `GET /tasks` — return all tasks as a list
- Implement `POST /tasks` — accept a task in the request body and add it to the collection, returning the created task
- Implement `PUT /tasks/{task_id}` — update the `title` or `completed` status of an existing task by ID
- Implement `DELETE /tasks/{task_id}` — remove a task by ID and return a confirmation message
- Return an appropriate HTTP 404 response when a task ID is not found

#### Example

```
POST /tasks
Body: {"id": 1, "title": "Learn FastAPI", "completed": false}
Response: {"id": 1, "title": "Learn FastAPI", "completed": false}

GET /tasks
Response: [{"id": 1, "title": "Learn FastAPI", "completed": false}]

DELETE /tasks/1
Response: {"message": "Task 1 deleted"}
```


### 🛠️ Add Query Parameters and Filter Support

#### Description
Extend the `GET /tasks` endpoint to support optional query parameters so clients can filter and search the task list without fetching everything.

#### Requirements
Completed program should:

- Accept an optional `completed` query parameter (boolean) to filter tasks by their completion status, e.g. `GET /tasks?completed=true`
- Accept an optional `search` query parameter (string) to return only tasks whose `title` contains the search term (case-insensitive), e.g. `GET /tasks?search=fastapi`
- Allow both parameters to be combined, e.g. `GET /tasks?completed=false&search=learn`
- Return an empty list `[]` when no tasks match the filters, rather than an error

#### Example

```
GET /tasks?completed=false
Response: [{"id": 2, "title": "Build an API", "completed": false}]

GET /tasks?search=api
Response: [{"id": 1, "title": "Learn FastAPI", "completed": true}, {"id": 2, "title": "Build an API", "completed": false}]
```
