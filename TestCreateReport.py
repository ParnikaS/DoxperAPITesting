from Settings import BaseSettings
import requests
import json
import os
import inspect

class TestCreateReportApi(BaseSettings):

    report_json_file = open(os.path.abspath('jsonfiles/CreateReport.json'), 'r')
    test_data = json.load(report_json_file)
    report_json_file.close()

    def test_aCreateWithoutGivingType(self):
        input = self.test_data["cases"][0]["input"]
        output = self.test_data["cases"][0]["expected_output"]
        self.apiCall(input, output)

    def test_bCreateWithoutPatientDetails(self):
        input = self.test_data["cases"][1]["input"]
        output = self.test_data["cases"][1]["expected_output"]
        self.apiCall(input, output)

    # def test_cCreateWithoutPatientId(self):
    #     input = self.test_data["cases"][2]["input"]
    #     output = self.test_data["cases"][2]["expected_output"]
    #     self.apiCall(input, output)

    def test_dCreateWithoutPageNum(self):
        input = self.test_data["cases"][3]["input"]
        output = self.test_data["cases"][3]["expected_output"]
        self.apiCall(input, output)

    # def test_eCreateWithoutUrl(self):
    #     input = self.test_data["cases"][4]["input"]
    #     output = self.test_data["cases"][4]["expected_output"]
    #     self.apiCall(input, output)

    def test_fCreateReport(self):
        input = self.test_data["cases"][4]["input"]
        output = self.test_data["cases"][4]["expected_output"]
        self.apiCall(input, output)

    def apiCall(self, inp, exp_out):
        api_url = self.base_url + self.test_data["api_endpoint"]
        data = requests.post(url=api_url, data= json.dumps(inp), headers = self.headers)
        statusCode = data.status_code
        print(statusCode)
        resp = data.json()
        print(resp)
        callingMethod = inspect.stack()[1][3]
        if statusCode == 200:
            # exp_out = resp
            # self.json_write_data(os.path.abspath('jsonfiles/CreateReport.json'), 'w')
            # assert self.test_data["cases"][index]["expected_output"]["id"] != ""
            assert resp.get("id")!= ""
        else:
            resp == exp_out
