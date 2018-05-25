import requests
import json
import os

class RestoreOldData():

    def SetOldPassword(self):
        inp = {"oldpassword":"t", "newpassword":"td"}
        # respone = requests.post()
        api_url = "https://test.doxper.com/api/update_password/"

        helper_file = open(os.path.abspath('jsonfiles/APIHelper.json'))
        test_data = json.load(helper_file)
        helper_file.close()

        print(test_data["headers"])
        data = requests.post(url=api_url, data=json.dumps(inp), headers=test_data["headers"])
        resp = data.json()
        token = resp.get('token')
        print(resp)
        test_data["headers"]["Authorization"] = 'Token ' + token

        with open(os.path.abspath('jsonfiles/APIHelper.json'), 'w') as file:
            file.write(json.dumps(test_data))
            file.close()
        print(test_data)

