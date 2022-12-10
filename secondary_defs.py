import allure
import json

def matching_status_code_assert(response: str, correct_code: int) -> None:
        """Matching response status code with correct code. If codes are not equal, raise AssertionError
        
        Args:
         - response: str from requests
         - correct_code: int like 200 or 404

        Raise AssertionError like 'Response code is wrong. Have to be 200, but have 400'
        """
        with allure.step("Matching status code and correct code"):
            if response.status_code != correct_code:
                raise AssertionError(f'Response code is wrong. Have to be {correct_code}, but have {response.status_code}')


def convert_response_to_dict(response: str) -> dict:
        """Convert response to dict type and return it
        
        Args:
        - response: str from requests
        """
        
        return response.json()

def get_data_from_dict(data: dict, key_list: list):
    for key in key_list:
        data = data.get(key)

    return data

def read_and_return_data(name_func: str, name_file: str) -> dict:
    """
    Return correct data for func from file_name
    name_func: key for dict (for example "get_sigle_user_not_found")
    name_file: name of your file with data (for example "data.json")
    """
    with open(f"{name_file}", 'r') as f:
        data = json.load(f)
        return data[name_func][0]