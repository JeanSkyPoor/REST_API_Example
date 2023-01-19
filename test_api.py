from api_methods import APIMethods


def test_get_list_users():

    APIMethods().\
        get_list_users(1).\
        matching_status_code_assert(200)
    

def test_get_single_user():

    APIMethods().\
        get_single_user(1).\
        matching_status_code_assert(200)


def test_get_single_user_not_found():

    APIMethods().\
        get_single_user(23).\
        matching_status_code_assert(404)


def test_post_create():

    APIMethods().\
        create_new_user().\
        matching_status_code_assert(201)


def test_update_user():

    APIMethods().\
        update_user(2).\
        matching_status_code_assert(200)


def test_delete_user():

    APIMethods().\
        delete_user(2).\
        matching_status_code_assert(204)


def test_register_successful():

    APIMethods().\
        register(successful = True).\
        matching_status_code_assert(200)


def test_register_unsuccessful():

    APIMethods().\
        register(successful = False).\
        matching_status_code_assert(400)


def test_login_successful():

    APIMethods().\
        login(successful = True).\
        matching_status_code_assert(200)


def test_login_unsuccessful():

    APIMethods().\
        login(successful = False).\
        matching_status_code_assert(400)