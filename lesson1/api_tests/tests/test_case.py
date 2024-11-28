from lesson1.api_tests.services.case.pom import create_case
from lesson1.api_tests.services.case.data import create_case_dict
from lesson1.api_tests.services.case.models import Case


def test_create_case():
    # or using model 
    # response = create_case(Case(**create_case_dict).model_dump())
    response = create_case(json=create_case_dict)
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(create_case_dict)
    # Also we can check schema
    # response.schema_should_be_eq(Case(**create_case_dict).model_json_schema())
