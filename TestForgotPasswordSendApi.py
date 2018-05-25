from Settings import BaseSettings
import requests
import json
import os

class TestForgotPasswordApi(BaseSettings):

    forgotPwd_json_file = open(os.path.abspath('jsonfiles/ForgotPasswordSend.json'),'r')
    test_data = json.load(forgotPwd_json_file)
    forgotPwd_json_file.close()

    def test_PassBlankAsNumber(self):
        pass

    def test_PassBlankAsReason(self):
        pass

    def test_NoDoctorForNumber(self):
        pass

    def test_MultipleDoctorForNumber(self):
        pass

    def test_OneDoctorForNumber(self):
        pass

    def test_1(self):
        pass

    def apiCall(self, inp, exp_out):
        pass