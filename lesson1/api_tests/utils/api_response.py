import allure
from deepdiff import DeepDiff
from jsonschema import ValidationError, validate
from requests import Response


class APIResponse:
    def __init__(self, response: Response):
        self.response = response

    def status_code_should_be_eq(self, expected_status):
        assert (
                self.response.status_code == expected_status
        ), f"Ожидали {expected_status}, но получили {self.response.status_code}"
        return self

    def len_of_json_should_be_eq(self, expected_len):
        assert (
                len(self.response.json()) == expected_len
        ), f"Ожидали {expected_len}, но получили {len(self.response.json())}"
        return self

    def json_should_be_eq(self, expected_json):
        try:
            response_json = self.response.json()
        except ValueError:
            raise AssertionError("Это не Json формат")

        diff = DeepDiff(
            response_json, expected_json, verbose_level=2, ignore_order=True
        )

        if diff:
            error_message = "JSON объекты отличаются:\n"

            if "dictionary_item_added" in diff:
                error_message += "Добавлены следующие элементы:\n"
                for item in diff["dictionary_item_added"]:
                    error_message += f"  {item}\n"

            if "dictionary_item_removed" in diff:
                error_message += "Удалены следующие элементы:\n"
                for item in diff["dictionary_item_removed"]:
                    error_message += f"  {item}\n"

            if "values_changed" in diff:
                error_message += "Изменены следующие значения:\n"
                for key, change in diff["values_changed"].items():
                    error_message += f"  {key}: с '{change['old_value']}' на '{change['new_value']}'\n"

            error_message += f"\nОжидаемый JSON:\n{expected_json}\n"
            error_message += f"Полученный JSON:\n{response_json}"
            raise AssertionError(error_message)

        return self

    def json_should_contains(self, expected_json):
        try:
            response_json = self.response.json()
        except ValueError:
            raise AssertionError("Это не Json формат")

        def compare(expected, actual):
            if isinstance(expected, dict):
                for key, expected_value in expected.items():
                    if key not in actual:
                        raise AssertionError(
                            f"Ключ '{key}' отсутствует в фактическом JSON."
                        )
                    compare(expected_value, actual[key])
            elif isinstance(expected, list):
                if len(expected) != len(actual):
                    raise AssertionError("Размеры списков не совпадают.")
                for e_item, a_item in zip(expected, actual):
                    compare(e_item, a_item)
            else:
                if expected != actual:
                    raise AssertionError(
                        f"Ожидаемое значение '{expected}', получено '{actual}'."
                    )

        compare(expected_json, response_json)
        return self

    def response_without_fields(self, *fields):
        return {k: v for k, v in self.response.json().items() if k not in fields}

    @allure.step("Валидируем схему")
    def schema_should_be_eq(self, expected_schema):
        try:
            response_json = self.response.json()
        except ValueError:
            raise AssertionError("Это не Json формат")

        try:
            validate(instance=response_json, schema=expected_schema)
        except ValidationError as e:
            raise AssertionError(f"Ошибка валидации схемы: {e}")

        return self

    def len_of_values_with_key(self, key_name):
        self._current_value = len(self.response.json()[key_name])
        return self

    def type_of_value_with_key(self, key_name):
        self._current_value = type(self.response.json()[key_name])
        return self

    def value_with_key(self, key_name):
        self._current_value = self.response.json()[key_name]
        return self

    def get_value_with_key(self, key_name):
        return self.response.json()[key_name]

    def should_be_eq(self, expected_value):
        assert (
                self._current_value == expected_value
        ), f"Ожидали {expected_value}, но получили {self._current_value}"
        return self
