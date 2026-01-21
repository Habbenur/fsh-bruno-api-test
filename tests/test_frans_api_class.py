import pytest
from tests.frans_api_helper_class import FransApiHelper

BASE_URL = "https://test-379574553568.us-central1.run.app"
API_KEY = "habbe-testar-2026-class"

helper = FransApiHelper(base_url=BASE_URL, api_key=API_KEY)

def test_create_student():
    student_id = helper.create_student(name="Student Alpha", age=22, grade="B")
    assert student_id is not None, "Failed to create student"
    print(f"Student created with ID: {student_id}")

def test_delete_student():
    student_id = helper.create_student(name="Student Beta", age=23, grade="C")
    status_code = helper.delete_student(student_id)
    assert status_code == 200, "Failed to delete student"
    print(f"Student with ID {student_id} deleted successfully.")

def test_create_and_delete_student():
    student_id = helper.create_student(name="Student Gamma", age=24, grade="A")
    assert student_id is not None, "Failed to create student"
    status_code = helper.delete_student(student_id)
    assert status_code == 200, "Failed to delete student after creation"

def test_update_student():
    student_id = helper.create_student(name="Student Delta", age=25, grade="B")
    assert student_id is not None, "Failed to create student"
    status_code = helper.update_student(student_id, name="Student Delta Updated", age=26, grade="A")
    assert status_code == 200, "Failed to update student"

def test_get_student():
    student_id = helper.create_student(name="Student Epsilon", age=27, grade="C")
    assert student_id is not None, "Failed to create student"
    student_data = helper.get_student(student_id)

    assert student_data["name"] == "Student Epsilon", "Student name does not match"
    assert student_data["age"] == 27, "Student age does not match"
    assert student_data["grade"] == "C", "Student grade does not match"

def test_get_all_students():
    students = helper.get_all_students()
    assert isinstance(students, list), "Expected a list of students"
    print(f"Total students retrieved: {len(students)}")
