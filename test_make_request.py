from urllib import response
import requests
import pytest

def test_get_personnummer_from_skatteverket():
    url = "https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763?_limit=10&_offset=0"
    response = requests.get(url) #Trigger a request to Skatteverket and save it to the variable 'response'

    assert response.status_code == 200, "Request failed"
    assert response.headers.get('Content-Type') == 'application/json;charset=utf-8', \
    "Content-Type is not application/json"

    print(response.json()) #Prints whole response body from Skatteverket, more than we need

    #How do we get only the results parts?
