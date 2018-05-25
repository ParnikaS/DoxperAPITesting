from Settings import BaseSettings
import unittest
import requests
import json
import os

class TestAccountApi(BaseSettings):

    account_json_file = open(os.path.abspath('jsonfiles/AccountCreation.json'), 'r')
    test_data = json.load(account_json_file)
    account_json_file.close()

    def test_aMissingFirstName(self):
        print('case1')
        input = self.test_data["cases"][0]["input"]
        output = self.test_data["cases"][0]["expected_output"]
        self.apiCall(input,output)

    def test_bMissingLastName(self):
        print('case2')
        input = self.test_data["cases"][1]["input"]
        output = self.test_data["cases"][1]["expected_output"]
        self.apiCall(input, output)

    def test_cMissingEmail(self):
        print('case3')
        input = self.test_data["cases"][2]["input"]
        output = self.test_data["cases"][2]["expected_output"]
        self.apiCall(input, output)

    def test_dInvalidEmail(self):
        print('case4')
        input = self.test_data["cases"][3]["input"]
        output = self.test_data["cases"][3]["expected_output"]
        self.apiCall(input, output)

    def test_eMissingContactNumber(self):
        print('case5')
        input = self.test_data["cases"][4]["input"]
        output = self.test_data["cases"][4]["expected_output"]
        self.apiCall(input, output)

    def test_fMissingCity(self):
        print('case6')
        input = self.test_data["cases"][5]["input"]
        output = self.test_data["cases"][5]["expected_output"]
        self.apiCall(input, output)

    def test_gMissingSpeciality(self):
        print('case7')
        input = self.test_data["cases"][6]["input"]
        output = self.test_data["cases"][6]["expected_output"]
        self.apiCall(input, output)

    def test_hMissingRegistration(self):
        print('case8')
        input = self.test_data["cases"][7]["input"]
        output = self.test_data["cases"][7]["expected_output"]
        self.apiCall(input, output)

    def test_iCreateAccountwithCorrectData(self):
        print('case9')
        input = self.test_data["cases"][8]["input"]
        output = self.test_data["cases"][8]["expected_output"]
        self.apiCall(input, output)

    def test_jCreatingAccountWithSameName(self):
        print('case10')
        input = self.test_data["cases"][9]["input"]
        output = self.test_data["cases"][9]["expected_output"]
        self.apiCall(input, output)

    def apiCall(self, inp, exp_out):
        api_url = self.base_url + self.test_data["api_endpoint"]
        data = requests.post(url=api_url, data=json.dumps(inp), headers=self.headers)
        resp = data.json()
        if data.status_code == 200:
            assert resp.get('id') != ""
            assert resp.get('username') == self.test_data["cases"][8]["input"]["first_name"]+'.'+self.test_data["cases"][8]["input"]["last_name"]
            print(self.test_data["cases"][8]["input"]["first_name"]+'.'+self.test_data["cases"][8]["input"]["last_name"])
        else:
            assert resp == exp_out

if __name__ == '__main__':
    unittest.main()