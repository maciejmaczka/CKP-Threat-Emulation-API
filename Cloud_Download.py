import requests
import json
import warnings

warnings.filterwarnings("ignore")
#service = "https://192.168.10.123:18194/tecloud/api/v1/file/"
service = 'https://te.checkpoint.com/tecloud/api/v1/file/'

headers = {'Authorization': '3ef8ad6d94f1bb039c62c49ee5badd98', 'te_cookie': 'rembember' }   # dobry


params = { "id" : "9f7a0d030d697a82bae4ddad55306e4b"}

req = requests.get( service + 'download' , params=params, verify=False)

print(req.text)

with open ("report.xml", "w") as report:
        report.write(req.text)



    #     5e5de275-a103-4f67-b55b-47532918fa59