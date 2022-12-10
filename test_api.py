from api_methods import APIMethods
from secondary_defs import *
import allure

def test_get_list_users():
    with allure.step("Step 1. Create request"):
        response = APIMethods.get_list_users(1)

    with allure.step("Step 2. Checking status code of response"):
        matching_status_code_assert(response, 200)

    with allure.step("Step 3. Convert response to dict"):
        data = convert_response_to_dict(response)
    
    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_response(data, ["page"])) == int, "Type of data by keys ['page'] is not int"
        assert type(get_data_from_response(data, ["per_page"])) == int, "Type of data by keys ['per_page'] is not int"
        assert type(get_data_from_response(data, ["total"])) == int, "Type of data by keys ['total'] is not int"
        assert type(get_data_from_response(data, ["total_pages"])) == int, "Type of data by keys ['total_pages'] is not int"
        assert type(get_data_from_response(data, ["data"])) == list, "Type of data by keys ['data'] is not list"

    
def test_get_single_user():
    with allure.step("Step 1. Create request"):
        response = APIMethods.get_single_user(1)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 200)

    with allure.step("Step 3. Convert response to dict"):
        data = convert_response_to_dict(response)
    
    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_response(data, ["data"])) == dict, "Type of data by keys ['data'] is not dict"
        assert type(get_data_from_response(data, ["data", "id"])) == int, "Type of data by keys ['data', 'id'] is not int"
        assert type(get_data_from_response(data, ["data", "email"])) == str, "Type of data by keys ['data', 'email'] is not str"
        assert type(get_data_from_response(data, ["data", "first_name"])) == str, "Type of data by keys ['data', 'first_name'] is not str"
        assert type(get_data_from_response(data, ["data", "last_name"])) == str, "Type of data by keys ['data', 'last_name'] is not str"
        assert type(get_data_from_response(data, ["data", "avatar"])) == str, "Type of data by keys ['data', 'avatar'] is not str"


def test_get_single_user_not_found():
    with allure.step("Step 1. Create request"):
        response = APIMethods.get_single_user(23)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 404)

    with allure.step("Step 3. Convert response to dict"):
        data = convert_response_to_dict(response)
    
    with allure.step("Step 4. Checking types of data"):
        assert len(data) == 0, 'Response is not empty, but have to be one'


def test_post_create():
    with allure.step("Step 1. Create request"):
        test_data = read_and_return_data('post_create', 'data.json')

        response = APIMethods.create_new_user(test_data)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 201)

    with allure.step("Step 3. Convert response to dict"):
        data = convert_response_to_dict(response)
    
    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_response(data, ["name"])) == str, "Type of data by keys ['name'] is not str"
        assert type(get_data_from_response(data, ["job"])) == str, "Type of data by keys ['job'] is not str"
        assert type(get_data_from_response(data, ["id"])) == str, "Type of data by keys ['id'] is not str"
        assert type(get_data_from_response(data, ["createdAt"])) == str, "Type of data by keys ['createdAt'] is not str"

    with allure.step("Step 5. Checking response data and test data"):
        assert get_data_from_response(data, ["name"]) == test_data.get('name'), "Name from response is not equal name from test data"
        assert get_data_from_response(data, ["job"]) == test_data.get('job'), "Job from response is not equal job from test data"


def test_update_user():
    with allure.step("Step 1. Create request"):
        test_data = read_and_return_data('put_update', 'data.json')

        response = APIMethods.update_user(test_data, 2)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 200)

    with allure.step("Step 3. Convert response to dict"):
        data = convert_response_to_dict(response)    
    
    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_response(data, ["name"])) == str, "Type of data by keys ['name'] is not str"
        assert type(get_data_from_response(data, ["job"])) == str, "Type of data by keys ['job'] is not str"
        assert type(get_data_from_response(data, ["updatedAt"])) == str, "Type of data by keys ['updatedAt'] is not str"
    
    with allure.step("Step 5. Checking response data and test data"):
        assert get_data_from_response(data, ["name"]) == test_data.get('name'), "Name from response is not equal name from test data"
        assert get_data_from_response(data, ["job"]) == test_data.get('job'), "Job from response is not equal job from test data"


def test_delete_user():
    with allure.step("Step 1. Create request"):
        response = APIMethods.delete_user(2)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 204)


def test_register_successful():
    with allure.step("Step 1. Create request"):
        test_data = read_and_return_data('post_register_successful', 'data.json')

        response = APIMethods.register(test_data)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 200)

    with allure.step("Step 3. Convert response to dict"):
        data = convert_response_to_dict(response)   

    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_response(data, ["id"])) == int, "Type of data by keys ['id'] is not int"
        assert type(get_data_from_response(data, ["token"])) == str, "Type of data by keys ['token'] is not str"


def test_register_unsuccessful():
    with allure.step("Step 1. Create request"):
        test_data = read_and_return_data('post_register_unsuccessful', 'data.json')

        response = APIMethods.register(test_data)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 400)

    with allure.step("Step 3. Convert response to dict"):
        data = convert_response_to_dict(response)  

    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_response(data, ["error"])) == str, "Type of data by keys ['error'] is not str"
     
    with allure.step("Step 5. Checking response data"):
        assert get_data_from_response(data, ["error"]) == "Missing password", 'Error message has uncorrect text'


def test_login_successful():
    with allure.step("Step 1. Create request"):
        test_data = read_and_return_data('post_login_successful', 'data.json')

        response = APIMethods.register(test_data)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 200)

    with allure.step("Step 3. Convert response to dict"):
        data = convert_response_to_dict(response)  

    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_response(data, ["token"])) == str, "Type of data by keys ['token'] is not str"


def test_login_unsuccessful():
    with allure.step("Step 1. Create request"):
        test_data = read_and_return_data('post_login_unsuccessful', 'data.json')

        response = APIMethods.register(test_data)

    with allure.step("Step 2. Checking response's status code"):
        matching_status_code_assert(response, 400)

    with allure.step("Step 3. Convert response to dict"):
        data = convert_response_to_dict(response)  

    with allure.step("Step 4. Checking types of data"):
        assert type(get_data_from_response(data, ["error"])) == str, "Type of data by keys ['error'] is not str"
    
    with allure.step("Step 5. Checking response data"):
        assert get_data_from_response(data, ["error"]) == "Missing password", 'Error message has uncorrect text'