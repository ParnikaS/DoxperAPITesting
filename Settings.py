from unittest import TestCase
import json
import os

class BaseSettings (TestCase):

    @classmethod
    def setUpClass(cls):
        print("in SetUP Class")
        helper_file = open(os.path.abspath('jsonfiles/APIHelper.json'))
        test_data = json.load(helper_file)
        helper_file.close()
        cls.headers = test_data["headers"]
        cls.base_url = test_data["base_url"]

    @classmethod
    def tearDownClass(cls):
        print("in tear down class")
        print("----Test is Over----")

    def json_read_data(self, jsonfile):
        with open(jsonfile, 'r') as file:
            dataset = json.load(file)
            file.close()
            return dataset

    def json_write_data(self, jsonfile, data):
        with open(jsonfile, 'w') as file:
            file.write(json.dumps(data))
            file.close()

    def inputOutputs(self, index):
        input = self.test_data["cases"][index]["input"]
        output = self.test_data["cases"][index]["expected_output"]
        self.apiCall(input, output)

    def apiCall(self, inp, exp_out):
        pass