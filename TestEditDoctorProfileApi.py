from Settings import BaseSettings
import requests
import json
import os

class TestEditProfileApi(BaseSettings):

    edit_json_file = open(os.path.abspath('jsonfiles/EditDoctorProfile.json'), 'r')
    test_data = json.load(edit_json_file)
    edit_json_file.close()

    def test_aEditRegistrationEmpty(self):
        print(self.test_data["cases"][0]["desc"])
        input = self.test_data["cases"][0]["input"]
        output = self.test_data["cases"][0]["expected_output"]
        self.apiCall(input, output)

    def test_bEditRegistration(self):
        print(self.test_data["cases"][1]["desc"])
        input = self.test_data["cases"][1]["input"]
        output = self.test_data["cases"][1]["expected_output"]
        self.apiCall(input, output)

    def test_cEditTitleEmpty(self):
        print(self.test_data["cases"][2]["desc"])
        input = self.test_data["cases"][2]["input"]
        output = self.test_data["cases"][2]["expected_output"]
        self.apiCall(input, output)

    # def test_dEditTitle(self):
    #     print(self.test_data["cases"][3]["desc"])
    #     input = self.test_data["cases"][3]["input"]
    #     output = self.test_data["cases"][3]["expected_output"]
    #     self.apiCall(input, output)

    def test_eEditFirstNameEmpty(self):
        print(self.test_data["cases"][3]["desc"])
        input = self.test_data["cases"][3]["input"]
        output = self.test_data["cases"][3]["expected_output"]
        self.apiCall(input, output)

    def test_fEditFirstName(self):
        print(self.test_data["cases"][4]["desc"])
        input = self.test_data["cases"][4]["input"]
        output = self.test_data["cases"][4]["expected_output"]
        self.apiCall(input, output)

    def test_gEditLasttNameEmpty(self):
        print(self.test_data["cases"][5]["desc"])
    #    print(self.test_data["cases"][5]["input"])
        input = self.test_data["cases"][5]["input"]
        output = self.test_data["cases"][5]["expected_output"]
      #  print(self.test_data["cases"][5]["expected_output"])
        self.apiCall(input, output)

    def test_hEditLastName(self):
        print(self.test_data["cases"][6]["desc"])
        input = self.test_data["cases"][6]["input"]
        output = self.test_data["cases"][6]["expected_output"]
        self.apiCall(input, output)

    def test_iEditUsernameEmpty(self):
        print(self.test_data["cases"][7]["desc"])
        input = self.test_data["cases"][7]["input"]
        output = self.test_data["cases"][7]["expected_output"]
        self.apiCall(input, output)

    def test_jEditUsernme(self):
        print(self.test_data["cases"][8]["desc"])
        input = self.test_data["cases"][8]["input"]
        output = self.test_data["cases"][8]["expected_output"]
        self.apiCall(input, output)

    def test_kEditCityNoIdBlankNameCitycode(self):
        print(self.test_data["cases"][9]["desc"])
        input = self.test_data["cases"][9]["input"]
        output = self.test_data["cases"][9]["expected_output"]
        self.apiCall(input, output)

    def test_lEditCitNoidEditedNameCitycode(self):
        print(self.test_data["cases"][10]["desc"])
        input = self.test_data["cases"][10]["input"]
        output = self.test_data["cases"][10]["expected_output"]
        self.apiCall(input, output)

    def test_mEditCityOnlyIdBlankNameCitycode(self):
        print(self.test_data["cases"][11]["desc"])
        input = self.test_data["cases"][11]["input"]
        output = self.test_data["cases"][11]["expected_output"]
        self.apiCall(input, output)

    def test_nEditCityMismatchedIdNameCitycode(self):
        print(self.test_data["cases"][12]["desc"])
        input = self.test_data["cases"][12]["input"]
        output = self.test_data["cases"][12]["expected_output"]
        self.apiCall(input, output)

    def test_oEditCityCorrectIdNameCitycode(self):
        print(self.test_data["cases"][13]["desc"])
        input = self.test_data["cases"][13]["input"]
        output = self.test_data["cases"][13]["expected_output"]

    def test_pEditContactEmpty(self):
        print(self.test_data["cases"][14]["desc"])
        input = self.test_data["cases"][14]["input"]
        output = self.test_data["cases"][14]["expected_output"]
        self.apiCall(input, output)

    def test_qEditContact(self):
        print(self.test_data["cases"][15]["desc"])
        input = self.test_data["cases"][15]["input"]
        output = self.test_data["cases"][15]["expected_output"]
        self.apiCall(input, output)

    def test_rEditEmailEmpty(self):
        print(self.test_data["cases"][16]["desc"])
        input = self.test_data["cases"][16]["input"]
        output = self.test_data["cases"][16]["expected_output"]
        self.apiCall(input, output)

    def test_sEditEmailInvalid(self):
        print(self.test_data["cases"][17]["desc"])
        input = self.test_data["cases"][17]["input"]
        output = self.test_data["cases"][17]["expected_output"]
        self.apiCall(input, output)

    def test_tEditEmail(self):
        print(self.test_data["cases"][18]["desc"])
        input = self.test_data["cases"][18]["input"]
        output = self.test_data["cases"][18]["expected_output"]
        self.apiCall(input, output)

    def test_uEditSpecialityEmpty(self):
        print(self.test_data["cases"][20]["desc"])
        input = self.test_data["cases"][20]["input"]
        output = self.test_data["cases"][20]["expected_output"]
        self.apiCall(input, output)

    def test_vEditSpeciality(self):
        print(self.test_data["cases"][19]["desc"])
        input = self.test_data["cases"][19]["input"]
        output = self.test_data["cases"][19]["expected_output"]
        self.apiCall(input, output)

    def test_AddWorkingDetails(self):
        pass

    def test_EditWorkingDetails(self):
        pass

    def apiCall(self, inp, exp_out):
        api_url = self.base_url + self.test_data["api_endpoint"]
        data = requests.put(url=api_url, data=json.dumps(inp), headers=self.headers)
        resp = data.json()
        assert resp == exp_out

