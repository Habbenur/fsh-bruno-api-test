from urllib import response
import requests
import pytest

base_url = "https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763"

def test_get_personnummer_from_skatteverket():
    url = "https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763?_limit=10&_offset=0"
    response = requests.get(url) #Trigger a request to Skatteverket and save it to the variable 'response'

    assert response.status_code == 200, "Request failed"

    assert response.headers.get('Content-Type') == 'application/json;charset=utf-8', \
    "Content-Type is not application/json"

    print(response.json()) #Prints whole response body from Skatteverket, more than we need

    print(response.json()["results"]) #Print only the 'results' part of the response body

    # Save list of social security numbers to a variable, for easier access
    list_of_personnummer = response.json()["results"]
    for personnummer in list_of_personnummer:
        print(personnummer.get("personnummer")) #Print each social security number in the list


def test_get_personnummer_from_skatteverket_limit_10():
    response = requests.get(base_url + "?_limit=10")

    print(response.json())

def test_get_personnummer_from_skatteverket_limit_params():
    params = {"_limit": 10}
    response = requests.get(base_url, params=params)
    
    print(response.json())  

@pytest.mark.parametrize("limit", [5, 10, 15])
def test_get_personnummer_from_skatteverket_limit_parametrize(limit):
    params = {"_limit": limit}
    response = requests.get(base_url, params=params)
    
    print(response.json())
    