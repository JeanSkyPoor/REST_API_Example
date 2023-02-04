from api_methods import APIMethods
from schemas import *
from faker import Faker
import pytest


@pytest.mark.parametrize("page_number, valid_schema, status_code", [[1, get_list_users_positive, 200],
                                                                    [2, get_list_users_positive, 200],

                                                                    [3, get_list_users_negative, 200],
                                                                    [7, get_list_users_negative, 200],
                                                                    [10, get_list_users_negative, 200]])
def test_get_list_users(page_number, valid_schema, status_code):

    APIMethods.get_list_users(page_number, valid_schema).\
        matching_status_code_assert(status_code)


@pytest.mark.parametrize("user_id, valid_schema, status_code, key_list, id", [[1, get_single_user_positive, 200, ["data", "id"], 1],
                                                                              [2, get_single_user_positive, 200, ["data", "id"], 2],
                                                                              [3, get_single_user_positive, 200, ["data", "id"], 3],

                                                                              [99, get_single_user_negative, 404, None, None],
                                                                              [103, get_single_user_negative, 404, None, None]])
def test_get_single_user(user_id, valid_schema, status_code, key_list, id):

    APIMethods.get_single_user(user_id, valid_schema).\
        matching_status_code_assert(status_code).\
        matching_data_from_response(key_list, id)


@pytest.mark.parametrize("test_data, valid_schema, status_code", [[{"email": "eve.holt@reqres.in", "password": "pistol"}, register_positive, 200],
                                                                    [{"email": Faker().email()}, register_negative, 400]])       
def test_register(test_data, valid_schema, status_code):
    APIMethods.register(test_data, valid_schema).\
        matching_status_code_assert(status_code)