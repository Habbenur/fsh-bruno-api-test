import pytest
import requests

#BaseURL is a coomon way of structure URLs to an API
base_url = "https://test-379574553568.us-central1.run.app/student"

def test_get_all_students():
    headers = {"API_KEY": "habbe-testar-2026"}
    response = requests.get(base_url, headers=headers)
    assert response.status_code == 200, "Request failed"
    print(response.json())

def test_create_a_student():
    '''Create a new student using Frans API.
    Endpoint: 
    POST/student
    Add a JSON with name, age,grade '''
    headers = {"API_KEY": "habbe-testar-2026", "Content-Type": "application/json"}
    
    #This is (student_data) a JSON object we want to send to the API to create a new student
    student_data = {
        "name": "Student ALPHA",
        "age": 20,
        "grade": "A"
    }
    response = requests.post(base_url, json=student_data, headers=headers)
    assert response.status_code in (200, 201), f"Failed to create student, status code: {response.status_code}"
    assert response.json()["status"] == "OK", "Student creation was not successful"
    #Possible also to assert that "id" not null, zero or below zero.
    print(response.json())

def test_get_student_by_id():
    '''Get a student by ID using Frans API.
    Endpoint: 
    GET/student/{id} '''
    student_id = 5  # Replace with a valid student ID
    headers = {"API_KEY": "habbe-testar-2026"}
    response = requests.get(f"{base_url}/{student_id}", headers=headers)
    assert response.status_code == 200, f"Failed to get student with ID {student_id}"
    print(response.json())

def test_update_student_by_id():
    '''Update a student by ID using Frans API.
    Endpoint: 
    PUT/student/{id}
    Add a JSON with name, age,grade '''
    student_id = 4  # Replace with a valid student ID
    headers = {"API_KEY": "habbe-testar-2026", "Content-Type": "application/json"}
    updated_student_data = {
        "name": "Student BETA UPDATED",
        "age": 21,
        "grade": "A+"
    }
    response = requests.put(f"{base_url}/{student_id}", json=updated_student_data, headers=headers)
    assert response.status_code == 200, f"Failed to update student with ID {student_id}"
    print(response.json())

def test_delete_student_by_id():
    '''Delete a student by ID using Frans API.
    Endpoint: 
    DELETE/student/{id} '''
    student_id = 3  # Replace with a valid student ID
    headers = {"API_KEY": "habbe-testar-2026"}
    response = requests.delete(f"{base_url}/{student_id}", headers=headers)
    assert response.status_code == 200, f"Failed to delete student with ID {student_id}"
    print(f"Student with ID {student_id} deleted successfully.")    