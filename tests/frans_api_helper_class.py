import requests

class FransApiHelper:
    """Helper functions for Frans API"""

    def __init__(self, base_url, api_key):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def create_student(self, name, age, grade):
        payload = {"name": name, "age": age, "grade": grade}
        headers = {"API_KEY": self.api_key, "Content-Type": "application/json"}

        response = requests.post(
            f"{self.base_url}/student",
            json=payload,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        return response.json()["student_id"]

    def delete_student(self, student_id):
        headers = {"API_KEY": self.api_key}

        response = requests.delete(
            f"{self.base_url}/student/{student_id}",
            headers=headers,
            timeout=10
        )
        return response.status_code

    def update_student(self, student_id, name=None, age=None, grade=None):
        payload = {}
        if name is not None:
            payload["name"] = name
        if age is not None:
            payload["age"] = age
        if grade is not None:
            payload["grade"] = grade

        headers = {"API_KEY": self.api_key, "Content-Type": "application/json"}

        response = requests.put(
            f"{self.base_url}/student/{student_id}",
            json=payload,
            headers=headers,
            timeout=10
        )
        return response.status_code

    def get_student(self, student_id):
        headers = {"API_KEY": self.api_key}

        response = requests.get(
            f"{self.base_url}/student/{student_id}",
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        return response.json()

    def get_all_students(self):
        headers = {"API_KEY": self.api_key}
        response = requests.get(
            f"{self.base_url}/student",
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
