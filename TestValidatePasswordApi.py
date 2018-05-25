import unittest
from Settings import BaseSettings
import json
import requests
import os

class TestValidatePassword(BaseSettings):

    validatePassword_file = open(os.path.abspath('jsonfiles/ValidatePassword.json'),'r')
    test_data = json.load(validatePassword_file)
    validatePassword_file.close()

    def setUp(self):
       pass

    def tearDown(self):
        pass

    def test_WrongPassword(self):
        input = self.test_data["cases"][0]["input"]
        output = self.test_data["cases"][0]["expected_output"]
        self.apiCall(input, output)

    def test_MissingPassword(self):
        input = self.test_data["cases"][1]["input"]
        output = self.test_data["cases"][1]["expected_output"]
        self.apiCall(input, output)

    def test_CorrectPassword(self):
        input = self.test_data["cases"][2]["input"]
        output = self.test_data["cases"][2]["expected_output"]
        self.apiCall(input, output)

    def apiCall(self, inp, exp_out):
        api_url = self.base_url + self.test_data["api_endpoint"]
        data = requests.post(url=api_url, data=json.dumps(inp), headers=self.headers)
        resp = data.json()
        assert resp == exp_out

if __name__ == '__main__':
    unittest.main()