from lesson1.api_tests.services.case.data import create_case_dict
from lesson1.api_tests.utils.api_client import client


### Get Read Root - GET
def test_get_read_root():
    response = client.make_request(handle="/", method="GET")
    response.status_code_should_be_eq(200)
    response.json_should_be_eq({"Hello": "World"})


### Get all TCs - GET
def test_get_testcases():
    response = client.make_request(
        handle="/testcases",
        method="GET",
    )
    response.status_code_should_be_eq(200)
    # not clear how to verify the list ?


### Create Test Case - POST
def test1_create_case():
    response = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": 3,
            "name": "Имя",
            "description": "Описание",
            "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
            "expected_result": "Ожидаемый результат",
            "priority": "низкий",
        },
    )
    response.status_code_should_be_eq(200)
    response.json_should_contains({"id": 3})


# OR
def test1_create_case1():
    response = client.make_request(
        handle="/testcases", method="POST", json=create_case_dict
    )
    response.status_code_should_be_eq(200)
    response.value_with_key("id").should_be_eq(0)


def test2_create_case_empty_data():
    """
    negative - body is empty
    """
    response = client.make_request(handle="/testcases", method="POST", json={})
    response.status_code_should_be_eq(422)
    response.json_should_be_eq(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "name"],
                    "msg": "Field required",
                    "input": {},
                },
                {
                    "type": "missing",
                    "loc": ["body", "description"],
                    "msg": "Field required",
                    "input": {},
                },
                {
                    "type": "missing",
                    "loc": ["body", "steps"],
                    "msg": "Field required",
                    "input": {},
                },
                {
                    "type": "missing",
                    "loc": ["body", "expected_result"],
                    "msg": "Field required",
                    "input": {},
                },
                {
                    "type": "missing",
                    "loc": ["body", "priority"],
                    "msg": "Field required",
                    "input": {},
                },
            ]
        }
    )


def test3_create_case_missed_priority_data():
    """
    negative - key "priority" is missing in the body
    """
    response = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": 0,
            "name": "string",
            "description": "string",
            "steps": ["string"],
            "expected_result": "string",
        },
    )
    response.status_code_should_be_eq(422)
    response.json_should_contains(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "priority"],
                    "msg": "Field required",
                    "input": {
                        "id": 0,
                        "name": "string",
                        "description": "string",
                        "steps": ["string"],
                        "expected_result": "string",
                    },
                }
            ]
        }
    )

### Get TC ID - GET
def test1_get_case_id():
    response1 = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": 4,
            "name": "Tom",
            "description": "Описание",
            "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
            "expected_result": "Ожидаемый результат",
            "priority": "низкий",
        },
    )

    case_id = response1.get_value_with_key("id")
    response2 = client.make_request(handle=f"/testcases/{case_id}", method="GET")
    response2.status_code_should_be_eq(200)
    response2.json_should_be_eq(
        {
            "id": 4,
            "name": "Tom",
            "description": "Описание",
            "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
            "expected_result": "Ожидаемый результат",
            "priority": "низкий",
        }
    )


def test2_get_case_not_existing_id():
    """
    negative - id is not exist
    """
    response2 = client.make_request(handle=f"/testcases/455", method="GET")
    response2.status_code_should_be_eq(404)
    response2.json_should_be_eq({"detail": "Test case not found."})


# not clear how to get Validation Error 422 ?


### To update TC data - PUT
def test1_update_case():
    response1 = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": 4,
            "name": "Tom",
            "description": "Описание",
            "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
            "expected_result": "Ожидаемый результат",
            "priority": "низкий",
        },
    )

    case_id = response1.get_value_with_key("id")
    response2 = client.make_request(
        handle=f"/testcases/{case_id}",
        method="PUT",
        json={
            "id": 5,
            "name": "string",
            "description": "string",
            "steps": ["string"],
            "expected_result": "string",
            "priority": "низкий",
        },
    )
    response2.status_code_should_be_eq(200)
    response2.json_should_be_eq(
        {
            "id": 5,
            "name": "string",
            "description": "string",
            "steps": ["string"],
            "expected_result": "string",
            "priority": "низкий",
        }
    )


def test2_update_case_empty_id():
    """
    negative = update to "id": ""
    """
    response1 = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": 4,
            "name": "Tom",
            "description": "Описание",
            "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
            "expected_result": "Ожидаемый результат",
            "priority": "низкий",
        },
    )

    case_id = response1.get_value_with_key("id")
    response2 = client.make_request(
        handle=f"/testcases/{case_id}",
        method="PUT",
        json={
            "id": "",
            "name": "string",
            "description": "string",
            "steps": ["string"],
            "expected_result": "string",
            "priority": "низкий",
        },
    )
    response2.status_code_should_be_eq(422)
    response2.json_should_be_eq(
        {
            "detail": [
                {
                    "type": "int_parsing",
                    "loc": ["body", "id"],
                    "msg": "Input should be a valid integer, unable to parse string as an integer",
                    "input": "",
                }
            ]
        }
    )


def test3_update_case_missed_description():
    """
    negative - description is missing in update body
    """
    response1 = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": 4,
            "name": "Tom",
            "description": "Описание",
            "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
            "expected_result": "Ожидаемый результат",
            "priority": "низкий",
        },
    )

    case_id = response1.get_value_with_key("id")
    response2 = client.make_request(
        handle=f"/testcases/{case_id}",
        method="PUT",
        json={
            "id": 2,
            "name": "string",
            "steps": ["string"],
            "expected_result": "string",
            "priority": "низкий",
        },
    )
    response2.status_code_should_be_eq(422)
    response2.json_should_be_eq(
        {
            "detail": [
                {
                    "type": "missing",
                    "loc": ["body", "description"],
                    "msg": "Field required",
                    "input": {
                        "id": 2,
                        "name": "string",
                        "steps": ["string"],
                        "expected_result": "string",
                        "priority": "низкий",
                    },
                }
            ]
        }
    )


### Delete TC
def test1_delete_case():
    response1 = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": 4,
            "name": "Tom",
            "description": "Описание",
            "steps": ["Шаг 1", "Шаг 2", "Шаг 3"],
            "expected_result": "Ожидаемый результат",
            "priority": "низкий",
        },
    )
    response1.status_code_should_be_eq(200)
    case_id = response1.get_value_with_key("id")
    response2 = client.make_request(
        handle=f"/testcases/{case_id}",
        method="DELETE",
    )
    response2.status_code_should_be_eq(200)
    response2.json_should_be_eq({"detail": "Test case deleted."})


def test2_delete_not_existing_case():
    """
    negative - delete not existing case
    """
    response2 = client.make_request(
        handle=f"/testcases/455",
        method="DELETE",
    )
    response2.status_code_should_be_eq(404)
    response2.json_should_be_eq({"detail": "Test case not found."})
