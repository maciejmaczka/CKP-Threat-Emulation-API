import requests
import json
import warnings

warnings.filterwarnings("ignore")
service = 'https://te.checkpoint.com/tecloud/api/v1/file/'
#service = "https://192.168.10.123:18194/tecloud/api/v1/file/"



headers = {'Authorization': 'TE_API_KEY_sooAWKFHoHrmuF4qcjuxvPR4g57GBcXSaWdvwab7', 'te_cookie': 'rembember' }   # dobry



request = {"request":
    {
    "md5": "3ef8ad6d94f1bb039c62c49ee5badd98"
    }}


#3ef8ad6d94f1bb039c62c49ee5badd98


req = requests.post(service + 'query' , headers=headers, data= json.dumps(request) , verify=False)
print(req.text)