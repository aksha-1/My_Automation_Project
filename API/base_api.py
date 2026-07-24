import requests
class APIClient:
    def __init__(self,base_url):
            self.base_url=base_url
            self.headers = {"Content-Type": "application/json"}
        


    def post(self,endpoint,payload):
        response=requests.post(
            url=self.base_url+endpoint,
            json=payload,
            headers=self.headers )
        return response



# import pytest
# import requests

# @pytest.mark.parametrize(
#     "user_id",
#     [1,2,3,4]
# )
# def test_get_user(user_id):

#     response = requests.get(
#         f"https://reqres.in/api/users/{user_id}"
#     )

#     assert response.status_code == 200