import requests
import json
import time
import warnings

warnings.filterwarnings("ignore")

service = "https://192.168.10.54:18194/tecloud/api/v1/file/"

request = { "request": [ { "md5" : "cbe82201c4e95173a3fdb84dd95998a3" ,  "features": [ "te"] } ] }

#request = {"request"  }


response = requests.post(service + 'query', data = json.dumps(request), verify=False)
responseText = json.loads(response.text)

print (responseText  )

