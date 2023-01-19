import requests
from env import BASE_LINK
import allure
import json


class APIMethods():

    def __init__(self) -> None:
        self.correct_status_code = None
        self.test_data = None
        self.response = None


    def get_list_users(self, page_number: int):
        """Get list of users from DB

        Args:
         - page_number: int, number of page we wanna get
        
        """        

        with allure.step("Create request"):
            self.response = requests.get(f'{BASE_LINK}/api/users?page={page_number}')

            return self


    def get_single_user(self, user_id: int):
        """Get user data from DB

        Args:
         - user_id: int, number of user we wanna get
        
        """

        with allure.step("Create request"):
            self.response = requests.get(f'{BASE_LINK}/api/users/{user_id}')

            return self


    def create_new_user(self):
        """Create new user. Using data from data.json for create user
        
        """
        with allure.step("prepare test data for request"):
            self.read_test_data('post_create', 'data.json')

        with allure.step("Create request"):
            self.response = requests.post(f'{BASE_LINK}/api/users/', data = self.test_data)

            return self


    def update_user(self, user_id: int):
        """Update user data

        Args:
         - user_id: int, number of user we wanna update
        
        """
        with allure.step("prepare test data for request"):
            self.read_test_data('put_update', 'data.json')

        with allure.step("Create request"):
            self.response = requests.put(f'{BASE_LINK}/api/users/{user_id}', data = self.test_data)

            return self


    def delete_user(self, user_id: int):
        """Delete user from BD using user_id
        
        Args:
         - user_id: int, number of user we wanna delete
        """

        with allure.step("Create request"):
            self.response = requests.delete(f'{BASE_LINK}/api/users/{user_id}')

            return self


    def register(self, successful: bool = True):
        """Register new user using data from data.json

        Args:
         - successful: bool, using correct data with True and uncorrect data with False 
        
        """
        if successful == True:
            with allure.step("prepare test data for request"):
                self.read_test_data('post_register_successful', 'data.json')
        else:
            with allure.step("prepare test data for request"):
                self.read_test_data('post_register_unsuccessful', 'data.json')

        with allure.step("Create request"):
            self.response = requests.post(f"{BASE_LINK}/api/register", data = self.test_data)

            return self


    def login(self, successful: bool = True):
        """Login in system

        Args:
         - successful: bool, using correct data with True and uncorrect data with False 
        
        """

        if successful == True:
            with allure.step("prepare test data for request"):
                self.read_test_data('post_login_successful', 'data.json')
        else:
            with allure.step("prepare test data for request"):
                self.read_test_data('post_login_unsuccessful', 'data.json')
        
        with allure.step("Create request"):
            self.response = requests.post(f"{BASE_LINK}/api/login", data = self.test_data)

            return self


    def matching_status_code_assert(self, correct_status_code: int) -> None:
        """Matching response status code with correct code. If codes are not equal, raise AssertionError
        
        Args:
         - correct_code: int like 200 or 404

        Raise AssertionError like 'Response code is wrong. Have to be 200, but have 400'
        """
        with allure.step("Matching status code and correct code"):
            if self.response.status_code != correct_status_code:
                raise AssertionError(f'Response code is wrong. Have to be {correct_status_code}, but have {self.response.status_code}')

            return self


    def convert_response_to_dict(self) -> dict:
            """Convert self.response to dict type"""
            self.response = self.response.json()

            return self


    def read_test_data(self, name_func: str, name_file: str) -> dict:
        """
        add test data in field self.test_data
        name_func: key for dict (for example "get_sigle_user_not_found")
        name_file: name of your file with data (for example "data.json")
        """
        with open(f"{name_file}", 'r') as f:
            data = json.load(f)
            self.test_data = data.get(name_func)[0]

            return self