#import unittest
from Settings import BaseSettings
import  json
import requests
from RestoreData import RestoreOldData
import os

class TestValidatePassword(BaseSettings):

    update_file = open(os.path.abspath('jsonfiles/UpdatePassword.json'))
    test_data = json.load(update_file)
    update_file.close()

    def test_aMissingNewPassword(self):
        input = self.test_data["cases"][0]["input"]
        output = self.test_data["cases"][0]["expected_output"]
        self.apiCall(input, output)

    def test_bMissingOldPassword(self):
        input = self.test_data["cases"][1]["input"]
        output = self.test_data["cases"][1]["expected_output"]
        self.apiCall(input, output)
#        self.method(self.INP2, self.OUT2)

    def test_cMissingBothPassword(self):
        input = self.test_data["cases"][2]["input"]
        output = self.test_data["cases"][2]["expected_output"]
        self.apiCall(input, output)
        #self.method(self.INP3, self.OUT3)


    def test_dWrongOldPassword(self):
        input = self.test_data["cases"][3]["input"]
        output = self.test_data["cases"][3]["expected_output"]
        self.apiCall(input, output)
        # self.method(self.INP4, self.OUT4)

    def test_esameNewPassword(self):
        input = self.test_data["cases"][4]["input"]
        output = self.test_data["cases"][4]["expected_output"]
        self.apiCall(input, output)

    def test_fCorrectNewPassword(self):
        input = self.test_data["cases"][5]["input"]
        output = self.test_data["cases"][5]["expected_output"]
        self.apiCall(input, output)

        # headers = json.dumps(self.headers)
        self.restore  = RestoreOldData()
        self.restore.SetOldPassword()

    def apiCall(self, inp, exp_out):
        api_url  = self.base_url + self.test_data["api_endpoint"]
        data = requests.post(url=api_url, data= json.dumps(inp), headers=self.headers)
        print(data)
        resp = data.json()
        print(resp)
        if data.status_code == 200:
            assert resp.get('details') == 'Updated'
            token = resp.get('token')
            helper_data= self.json_read_data(os.path.abspath('jsonfiles/APIHelper.json'))
            helper_data["headers"]["Authorization"] = 'Token ' + token
            self.headers["Authorization"] = 'Token ' + token
            self.json_write_data(os.path.abspath('jsonfiles/APIHelper.json'), helper_data)
            print(helper_data)
        else:
            assert resp == exp_out

if __name__ == '__main__':
      BaseSettings.unittest.main()