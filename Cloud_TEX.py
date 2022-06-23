import requests
import json
import warnings

warnings.filterwarnings("ignore")


#service = "https://192.168.10.123:18194/tecloud/api/v1/file/"
service = 'https://te.checkpoint.com/tecloud/api/v1/file/'



headers = {'Authorization': 'TE_API_KEY_rqH1ypNhoMaq6m6fTjoFJon0BcBtPm3bCCf7ulQF', 'te_cookie': 'rembember' }   # dobry


with open('D:\\Soft\\aaaa.docx' , encoding="utf8" ,  errors='ignore') as sample:

    request = {"request":
        {
        "file_name": "bbb.docx",
        "file_type" : "docx",
      #   "features": ["tex" ],
         "features": ["extraction"],
        }}

    files = {"file" : (sample) , 'request': json.dumps(request)}



    req = requests.post(service + 'upload' , files=files, headers=headers, verify=False)
    print(req.text)
