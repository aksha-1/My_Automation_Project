import requests
import pytest
from API.base_api import APIClient
from utilities.readProperties import ReadConfig
from TestData import employee_payload_api 
from utilities.custome_logger import LogGen
class TestAPI:
    log=LogGen.log_gen()

    @pytest.mark.api
    def test_create_product(self):
        self.log.info("****** API - test_create_product ****************")
        base_url=ReadConfig.get_base_url_api()
        payload=employee_payload_api.json_holder
        api_client=APIClient(base_url)
        end_point='/posts'
        self.log.info(f"****** End Point{end_point} ****************")
        response=api_client.post(end_point,payload)
        assert response.status_code==201

        self.log.info(f"****** Response code verified successfully ****************")

        body=response.json()
        assert body['title']==payload['title'], f'expected:{payload['title']}but got:{body['title']} '

        assert body['id'] is not None,f'expected:{ body['id']}but got: None '

        assert  type(body['userId'])==int,f'expected type int :but got:{type(body['userId'])} '

        self.log.info(f"****** Json body verified successfully  ****************")



