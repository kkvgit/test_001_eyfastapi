from fastapi.testclient import TestClient
import main

client = TestClient(main.appl)

def test_add():
    response = client.post("/add/", json={"batchID":'id0101', "payload": [[1, 2], [3,4]]})
    print(response.json())

def test_add_empty_list():
    response = client.post("/add/", json={"batchID":'id0102', "payload": []})
    print(response.json())

def test_add_invalid_input():
    response = client.post("/add/", json={"batchID":'id0103', "payload": [[1, 2], ['a', 'b']]})
    print(response.json())

test_add()
test_add_empty_list()
test_add_invalid_input()