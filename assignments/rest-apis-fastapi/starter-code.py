from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

# TODO: Add more students to this list
students = [
    {"id": 1, "name": "Alice", "grade": 10},
    {"id": 2, "name": "Bob", "grade": 11},
    {"id": 3, "name": "Carol", "grade": 10},
]


# TODO: Task 1 - Define a GET / endpoint that returns a welcome message
@app.get("/")
def root():
    pass  # Replace with your implementation


# TODO: Task 1 - Define a GET /students endpoint that returns the full student list
# TODO: Task 2 - Add an optional `grade` query parameter to filter results
@app.get("/students")
def get_students(grade: Optional[int] = None):
    pass  # Replace with your implementation


# TODO: Task 2 - Define a GET /students/{student_id} endpoint
# Return the matching student, or raise an HTTPException with status 404 if not found
@app.get("/students/{student_id}")
def get_student(student_id: int):
    pass  # Replace with your implementation
