from lesson1.api_tests.utils.api_client import client


def create_case(json={}):
    response = client.make_request(handle="/testcases", method="POST", json=json)

    return response
