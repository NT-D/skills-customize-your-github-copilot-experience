# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework in Python. You will learn how to define routes, handle HTTP methods, use path and query parameters, and return JSON responses.

## 📝 Tasks

### 🛠️ Task 1: Set Up a FastAPI Application

#### Description
Create a FastAPI application with a root endpoint and at least one additional route that returns structured JSON data.

#### Requirements
Completed program should:

- Import and instantiate a `FastAPI` app
- Define a `GET /` endpoint that returns a welcome message as JSON (e.g., `{"message": "Welcome to the Student API"}`)
- Define a `GET /students` endpoint that returns a hardcoded list of at least 3 students, each with an `id`, `name`, and `grade` field
- Run the application using `uvicorn` from the command line

### 🛠️ Task 2: Add Path Parameters and Query Parameters

#### Description
Extend the API to support retrieving a single student by ID using a path parameter, and filtering students by grade using a query parameter.

#### Requirements
Completed program should:

- Define a `GET /students/{student_id}` endpoint that returns a single student matching the given `student_id`
- Return a `404` HTTP status code with an error message if the student is not found
- Define a `GET /students` endpoint that accepts an optional `grade` query parameter to filter the list (e.g., `/students?grade=10`)
- Return only students matching the requested grade when the parameter is provided

```
# Example request and response
GET /students/1
→ {"id": 1, "name": "Alice", "grade": 10}

GET /students/99
→ {"detail": "Student not found"}

GET /students?grade=10
→ [{"id": 1, "name": "Alice", "grade": 10}]
```
