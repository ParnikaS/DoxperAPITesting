import unittest
from Settings import BaseSettings
import json
import requests
import os

class TestLoginApi(BaseSettings):


    login_json_file = open(os.path.abspath('jsonfiles/Login.json'), 'r')
    test_data = json.load(login_json_file)
    login_json_file.close()

    def test_aLogin_with_missing_username(self):
        #print(self.base_url)
        self.inputOutputs(0)
        #
        # input = self.test_data["cases"][0]["input"]
        # output = self.test_data["cases"][0]["expected_output"]
        # self.apiCall(input, output)

    # def test_bLogin_with_missing_password(self):
    #     input = self.test_data["cases"][1]["input"]
    #     output = self.test_data["cases"][1]["expected_output"]
    #     self.apiCall(input, output)
    #
    # def test_cLogin_with_wrong_credentials(self):
    #     input = self.test_data["cases"][2]["input"]
    #     output = self.test_data["cases"][2]["expected_output"]
    #     self.apiCall(input,output)
    #
    # def test_dLogin_with_missing_credentials(self):
    #     input = self.test_data["cases"][3]["input"]
    #     output = self.test_data["cases"][3]["expected_output"]
    #     self.apiCall(input, output)
    #
    # def test_eLogin_with_wrong_username(self):
    #     input = self.test_data["cases"][4]["input"]
    #     output = self.test_data["cases"][4]["expected_output"]
    #     self.apiCall(input, output)
    #
    # def test_fLogin_with_wrong_password(self):
    #     input = self.test_data["cases"][5]["input"]
    #     output = self.test_data["cases"][5]["expected_output"]
    #     self.apiCall(input, output)
    #
    # def test_gLogin_with_correct_credentials(self):
    #     input = self.test_data["cases"][6]["input"]
    #     output = self.test_data["cases"][6]["expected_output"]
    #     self.apiCall(input, output)

    def apiCall(self, inp, exp_out):
        api_url = self.base_url + self.test_data["api_endpoint"]
        data = requests.post(url=api_url, data=inp)
        statusCode = data.status_code

        if statusCode == 200:
            resp = data.json()
            print(resp)
            assert resp.get('token') != ""
            token = resp.get('token')
            helper_data= self.json_read_data(os.path.abspath('jsonfiles/APIHelper.json'))
            helper_data["headers"]["Authorization"] = 'Token ' + token
            self.json_write_data(os.path.abspath('jsonfiles/APIHelper.json'), helper_data)
        elif statusCode ==500:
            raise AssertionError
        else:
            assert data.json() == exp_out
if __name__ == '__main__':
    unittest.main()
