import requests
import allure
from env import BASE_LINK
from classes import ResponseData
from jsonschema import validate


class APIMethods():

    @staticmethod
    def get_list_users(page_number: int, valid_schema: dict):
        """Get list of users from DB

        Args:
         - page_number: int, number of page we wanna get
         - valid_schema: item from schemas.py for this method
        """
        with allure.step("Create request"):
            response = requests.get(f'{BASE_LINK}/api/users?page={page_number}')

        with allure.step("Validate response by valid schema"):
            validate(instance = response.json(), schema = valid_schema)

            return ResponseData(response)


    @staticmethod
    def get_single_user(user_id: int, valid_schema: dict):
        """Get user data from DB

        Args:
         - user_id: int, number of user we wanna get
         - valid_schema: item from schemas.py for this method
        
        """

        with allure.step("Create request"):
            response = requests.get(f'{BASE_LINK}/api/users/{user_id}')

        with allure.step("Validate response by valid schema"):
            validate(instance = response.json(), schema = valid_schema)
            return ResponseData(response)


    @staticmethod
    def register(test_data: dict, valid_schema: dict):
        """Register new user using data from data.json        
        """

        with allure.step("Create request"):
            response = requests.post(f"{BASE_LINK}/api/register", data = test_data)

        with allure.step("Validate response by valid schema"):
            validate(instance = response.json(), schema = valid_schema)
            return ResponseData(response)