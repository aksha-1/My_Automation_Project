import pytest
import requests

@pytest.mark.parametrize(
    "user_id",
    [1,2,3,4]
)
def test_get_user(user_id):

    response = requests.get(
        f"https://reqres.in/api/users/{user_id}"
    )

    assert response.status_code == 200