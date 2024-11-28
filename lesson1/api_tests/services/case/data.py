create_case_dict = {
    "id": 0,
    "name": "Тестовое задание",
    "description": "Тестовое задание",
    "priority": "высокий",
    "steps": ["шаг 1", "шаг 2", "шаг 3"],
    "expected_result": "Задание выполнено",
}


schema_response_empty_data = {
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