from schemas import *
from faker import Faker

testing_data = {
    "test_get_list_users": [[1, get_list_users_positive, 200],
                            [2, get_list_users_positive, 200],
                            [3, get_list_users_negative, 200],
                            [7, get_list_users_negative, 200],
                            [10, get_list_users_negative, 200]],

    "test_get_single_user": [[1, get_single_user_positive, 200, ["data", "id"], 1],
                            [2, get_single_user_positive, 200, ["data", "id"], 2],
                            [3, get_single_user_positive, 200, ["data", "id"], 3],
                            [99, get_single_user_negative, 404, None, None],
                            [103, get_single_user_negative, 404, None, None]],

    "test_register": [[{"email": "eve.holt@reqres.in", "password": "pistol"}, register_positive, 200],
                    [{"email": Faker().email()}, register_negative, 400]]
}
