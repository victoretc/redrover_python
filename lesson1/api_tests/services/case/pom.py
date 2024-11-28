from lesson1.api_tests.utils.api_client import client
from lesson1.api_tests.services.case.data import create_case_dict


def create_case(json={}):
    response = client.make_request(handle="/testcases", method="POST", json=json)
    return response


def get_read_root():
    response = client.make_request(
        handle="/",
        method="GET"
    )
    return response


def read_cases():
    response = client.make_request(
        handle="/testcases",
        method="GET",
    )
    return response


def read_case():
    response = create_case(json=create_case_dict)
    case_id = response.get_value_with_key("id")
    response = client.make_request(
        handle=f"/testcases/{case_id}",
        method="GET",
    )
    return response


def get_case_id():
    response = create_case(json=create_case_dict)
    case_id = response.get_value_with_key("id")
    return case_id


def update_case():
    case_id = get_case_id()
    response = client.make_request(
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
    return response


def delete_case():
    case_id = create_case(json=create_case_dict).get_value_with_key("id")
    response = client.make_request(
        handle=f"/testcases/{case_id}",
        method="DELETE",
    )
    return response
