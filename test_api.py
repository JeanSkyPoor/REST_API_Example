from api_methods import APIMethods
from schemas import *
import pytest
from classes import TestData

@pytest.mark.parametrize("page_number, valid_schema, status_code", TestData.return_data("test_get_list_users"))
def test_get_list_users(page_number, valid_schema, status_code):

    APIMethods.get_list_users(page_number, valid_schema).\
        matching_status_code_assert(status_code)


@pytest.mark.parametrize("user_id, valid_schema, status_code, key_list, id", TestData.return_data("test_get_single_user"))
def test_get_single_user(user_id, valid_schema, status_code, key_list, id):

    APIMethods.get_single_user(user_id, valid_schema).\
        matching_status_code_assert(status_code).\
        matching_data_from_response(key_list, id)


@pytest.mark.parametrize("test_data, valid_schema, status_code", TestData.return_data("test_register"))       
def test_register(test_data, valid_schema, status_code):
    APIMethods.register(test_data, valid_schema).\
        matching_status_code_assert(status_code)