from lesson1.api_tests.services.case.pom import create_case, get_read_root, read_cases, get_case_id, update_case, \
    delete_case
from lesson1.api_tests.services.case.data import create_case_dict, schema_response_empty_data
from lesson1.api_tests.services.case.models import Case
from lesson1.api_tests.utils.api_client import client


### Get Read Root - GET
def test_get_read_root():
    response = get_read_root()
    response.status_code_should_be_eq(200)
    response.json_should_be_eq({"Hello": "World"})


### Get all TCs - GET
def test_get_testcases():
    response = read_cases()
    response.status_code_should_be_eq(200)


### Create Test Case - POST
def test_create_case():
    response = create_case(Case(**create_case_dict).model_dump())
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(create_case_dict)
    response.schema_should_be_eq(Case(**create_case_dict).model_json_schema())


def test2_create_case_empty_data():
    """
    negative - body is empty
    """
    response = create_case()
    response.status_code_should_be_eq(422)
    response.json_should_be_eq(schema_response_empty_data)


def test3_create_case_missed_priority_data():
    """
    negative - key "priority" is missing in the body
    """
    response = create_case(json={
        "id": 0,
        "name": "string",
        "description": "string",
        "steps": ["string"],
        "expected_result": "string"
    }, )

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
    response = read_cases()
    response.status_code_should_be_eq(200)
    # response.schema_should_be_eq(Case(**create_case_dict).model_json_schema())


def test2_get_case_not_existing_id():
    """
    negative - id is not exist
    """
    response2 = client.make_request(handle=f"/testcases/455", method="GET")
    response2.status_code_should_be_eq(404)
    response2.json_should_be_eq({"detail": "Test case not found."})


### To update TC data - PUT
def test1_update_case():
    response = update_case()
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(
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
    case_id = get_case_id()

    response = client.make_request(
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
    response.status_code_should_be_eq(422)
    response.json_should_be_eq(
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
    negative - description is missing in body update
    """
    case_id = get_case_id()
    response = client.make_request(
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
    response.status_code_should_be_eq(422)
    response.json_should_be_eq(
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
    response = delete_case()
    response.status_code_should_be_eq(200)
    response.json_should_be_eq({"detail": "Test case deleted."})


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
