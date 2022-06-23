import requests
import json
import time
import warnings

warnings.filterwarnings("ignore")

service = "https://192.168.10.54:18194/tecloud/api/v1/file/"


with open('D:\\Soft\\aaaa.doc' ) as pliczek:

    request = {
        "request": {


        "file_name": "MyFile1.docx",
        "file_type": "doc",

         "features": ['extraction'],
         "extraction": {"method": "convert"}

    }}

    files = { 'file': pliczek , 'request' : json.dumps(request)}

    print(files)

    req = requests.post(service + 'upload' , files=files, verify=False)

    print(req.text)



