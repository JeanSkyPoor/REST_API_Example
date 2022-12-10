from api_methods import APIMethods
from secondary_defs import *
import allure
import pytest


@pytest.mark.parametrize("page_number, correct_code", [(1, 200), (2, 200), (3, 200)])
def test_get_list_users(page_number, correct_code):

    with allure.step("Step 1. Create request"):
        response = APIMethods.get_list_users(page_number)

    with allure.step("Step 2. Checking status code of response"):
        matching_status_code_assert(response, correct_code)

    with allure.step("Step 3. Convert respose to dict"):
        data = convert_response_to_dict(response)
    
    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_dict(data, ["page"])) == int, "Type of data by keys ['page'] is not int"
        assert type(get_data_from_dict(data, ["per_page"])) == int, "Type of data by keys ['per_page'] is not int"
        assert type(get_data_from_dict(data, ["total"])) == int, "Type of data by keys ['total'] is not int"
        assert type(get_data_from_dict(data, ["total_pages"])) == int, "Type of data by keys ['total_pages'] is not int"
        assert type(get_data_from_dict(data, ["data"])) == list, "Type of data by keys ['data'] is not list"
        assert type(get_data_from_dict(data, ["support"])) == dict, "Type of data by keys ['support'] is not dict"
    



