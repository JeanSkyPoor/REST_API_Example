from api_methods import APIMethods
from secondary_defs import *
import allure
import pytest



def test_get_list_users():
    with allure.step("Step 1. Create request"):
        response = APIMethods.get_list_users(1)

    with allure.step("Step 2. Checking status code of response"):
        matching_status_code_assert(response, 200)

    with allure.step("Step 3. Convert respose to dict"):
        data = convert_response_to_dict(response)
    
    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_dict(data, ["page"])) == int, "Type of data by keys ['page'] is not int"
        assert type(get_data_from_dict(data, ["per_page"])) == int, "Type of data by keys ['per_page'] is not int"
        assert type(get_data_from_dict(data, ["total"])) == int, "Type of data by keys ['total'] is not int"
        assert type(get_data_from_dict(data, ["total_pages"])) == int, "Type of data by keys ['total_pages'] is not int"
        assert type(get_data_from_dict(data, ["data"])) == list, "Type of data by keys ['data'] is not list"

    
def test_get_single_user():
    with allure.step("Step 1. Create request"):
        response = APIMethods.get_single_user(1)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 200)

    with allure.step("Step 3. Convert respose to dict"):
        data = convert_response_to_dict(response)
    
    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_dict(data, ["data"])) == dict, "Type of data by keys ['data'] is not dict"
        assert type(get_data_from_dict(data, ["data", "id"])) == int, "Type of data by keys ['data', 'id'] is not int"
        assert type(get_data_from_dict(data, ["data", "email"])) == str, "Type of data by keys ['data', 'email'] is not str"
        assert type(get_data_from_dict(data, ["data", "first_name"])) == str, "Type of data by keys ['data', 'first_name'] is not str"
        assert type(get_data_from_dict(data, ["data", "last_name"])) == str, "Type of data by keys ['data', 'last_name'] is not str"
        assert type(get_data_from_dict(data, ["data", "avatar"])) == str, "Type of data by keys ['data', 'avatar'] is not str"


def test_get_single_user_not_found():
    with allure.step("Step 1. Create request"):
        response = APIMethods.get_single_user(23)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 404)

    with allure.step("Step 3. Convert respose to dict"):
        data = convert_response_to_dict(response)
    
    with allure.step("Step 4. Checking types of data"):
        assert len(data) == 0, 'Response is not empty, but have to be one'


def test_post_create():
    with allure.step("Step 1. Create request"):
        request_body = read_and_return_data('post_create', 'data.json')

        response = APIMethods.create_new_user(request_body)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 201)

    with allure.step("Step 3. Convert respose to dict"):
        data = convert_response_to_dict(response)
    
    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_dict(data, ["name"])) == str, "Type of data by keys ['name'] is not str"
        assert type(get_data_from_dict(data, ["job"])) == str, "Type of data by keys ['job'] is not str"
        assert type(get_data_from_dict(data, ["id"])) == str, "Type of data by keys ['name'] is not str"
        assert type(get_data_from_dict(data, ["createdAt"])) == str, "Type of data by keys ['name'] is not str"

    with allure.step("Step 5. Checking respose data and test data"):
        assert get_data_from_dict(data, ["name"]) == request_body.get('name'), "Name from response is not equal name from test data"
        assert get_data_from_dict(data, ["job"]) == request_body.get('job'), "Job from response is not equal job from test data"