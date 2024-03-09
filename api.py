import http.client
import json
from urllib import parse
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from os import getenv

conn = http.client.HTTPSConnection("login.microsoftonline.com")
payload = json.dumps({
  "username": "oscar.webb162@education.nsw.gov.au"
})
headers = {
  'Content-Type': 'application/json',
}
conn.request("POST", "/common/GetCredentialType", payload, headers)
res = conn.getresponse()
data = res.read()
json = json.loads(data)
redirecturl = parse.urlparse(json["Credentials"]["FederationRedirectUrl"])

conn = http.client.HTTPSConnection("fs.det.nsw.edu.au")
conn.request("GET", redirecturl.path)
res = conn.getresponse()
data = res.read()

html = BeautifulSoup(data.decode("utf-8"), 'lxml')

load_dotenv('password.env')
password = getenv('PASSWORD')

payload = f'UserName=oscar.webb162&Password={password}&AuthMethod=FormsAuthentication'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

conn = http.client.HTTPSConnection("fs.det.nsw.edu.au")
url = html.form["action"]
parsedurl = parse.urlparse(url)
url = parsedurl.path + "?username=oscar.webb162%40education.nsw.gov.au&" + parsedurl.query

conn.request("POST", url, payload)
res = conn.getresponse()
data = res.read()
print(data)
