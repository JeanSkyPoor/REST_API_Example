import requests
from env import BASE_LINK





class APIMethods():
    @staticmethod
    def get_list_users(page_number: int) -> str:        

        response = requests.get(f'{BASE_LINK}/api/users?page={page_number}')

        return response

    @staticmethod
    def get_single_user(user_id: int) -> str:

        response = requests.get(f'{BASE_LINK}/api/users/{user_id}')

        return response

    @staticmethod
    def create_new_user(request_body: str) -> str:

        response = requests.post(f'{BASE_LINK}/api/users/', json = request_body)

        return response

    @staticmethod
    def update_user(request_body: str, user_id: int) -> str:

        response = requests.put(f'{BASE_LINK}/api/users/{user_id}', json = request_body)

        return response

    @staticmethod
    def delete_user(user_id: int) -> str:
        
        response = requests.delete(f'{BASE_LINK}/api/users/{user_id}')

        return response

    @staticmethod
    def register(request_body: str) -> str:

        response = requests.post(f"{BASE_LINK}/api/register", json = request_body)

        return response

    @staticmethod
    def login(request_body: str) -> str:

        response = requests.post(f"{BASE_LINK}/api/login", json = request_body)

        return response