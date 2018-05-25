from Settings import BaseSettings
import requests
import json
import os

class TestForgotPasswordApi(BaseSettings):

    forgotPwd_json_file = open(os.path.abspath('jsonfiles/ForgotPasswordSend.json'),'r')
    test_data = json.load(forgotPwd_json_file)
    forgotPwd_json_file.close()

    def test_BlankNumberBlankOtp(self):
        pass

    def test_BlankNumberRightOtp(self):
        pass

    def test_RightNumberBlankOtp(self):
        pass

    def test_WrongNumberWrongOtp(self):
        pass

    def test_WrongNumberRightOtp(self):
        pass

    def test_RightNumberWrongOtp(self):
        pass

    def test_RightNumberRightOtp(self):
        pass

    def apiCall(self, inp, exp_out):
        pass