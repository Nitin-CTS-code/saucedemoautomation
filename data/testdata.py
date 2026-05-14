# testdata/test_data.py

class TestData:
    base_url = "https://www.saucedemo.com"

    valid_creds = {
        "username": "standard_user",
        "password": "secret_sauce"
    }

    invalid_creds = {
        "username": "wrong_user",
        "password": "wrong_pass"
    }

print(TestData.invalid_creds)