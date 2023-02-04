import allure
import json
from testing_data import test_data


class ResponseData():
    def __init__(self, response) -> None:
        self.status_code = response.status_code
        self.text = response.text
        self.converted_responce = response.json()


    def matching_status_code_assert(self, correct_status_code: int):
        """Matching response status code with correct code. If codes are not equal, raise AssertionError
        
        Args:
         - correct_code: int like 200 or 404

        Raise AssertionError like 'Response code is wrong. Have to be 200, but have 400'
        """
        with allure.step("Matching status code and correct code"):
            if self.status_code != correct_status_code:
                raise AssertionError(f'Response code is wrong. Have to be {correct_status_code}, but have {self.status_code}')

            return self
            

    def matching_data_from_response(self, key_list: list, correct_data):
        if key_list == None:
            return self

        data = self.converted_responce
        for key in key_list:
            data = data.get(key)
        
        if correct_data != data:
            raise AssertionError(f"Data is wrong. Have to be {correct_data}, but have {data}. Keys list is {key_list}") 
        return self


class TestData():
    
    def return_data(test_name: str):
        return test_data[test_name]