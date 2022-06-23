import requests
import json
import time
import warnings
import ssl
PYTHONHTTPSVERIFY=0

warnings.filterwarnings("ignore")

service = "https://192.168.10.54:18194/tecloud/api/v1/file/"


files = { 'file': open('D:\\Soft\\aaa.docx', 'rb')}

req = requests.post(service + 'upload', files=files, verify=False)

print(req.text)

#gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
#info = urllib2.urlopen(req, context=gcontext).read()
#

#print(r.text)


