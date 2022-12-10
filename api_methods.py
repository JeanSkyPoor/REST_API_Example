import requests
from env import BASE_LINK
import json
import allure





class APIMethods():

    def get_list_users(self, page_number: int) -> str:        

        response = requests.get(f'{BASE_LINK}/api/users?page={page_number}')

        return response


    def get_single_user(self, user_id: int) -> str:

        response = requests.get(f'{BASE_LINK}/api/users/{user_id}')

        return response

    
    def create_new_user(self, request_body: str) -> str:

        response = requests.post(f'{BASE_LINK}/api/users/', json = request_body)

        return response

    
    def update_user(self, request_body: str, user_id: int) -> str:

        response = requests.put(f'{BASE_LINK}/api/users/{user_id}', json = request_body)

        return response

    
    def delete_user(self, user_id: int) -> str:
        
        response = requests.delete(f'{BASE_LINK}/api/users/{user_id}')

        return response


    def register(self, request_body: str) -> str:

        response = requests.post(f"{BASE_LINK}/api/register", json = request_body)

        return response


    def login(self, request_body: str) -> str:

        response = requests.post(f"{BASE_LINK}/api/login", json = request_body)

        return response