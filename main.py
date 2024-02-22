from requests import *
from conversion import convertjson

headers = {
	'Cookie': '_ga=GA1.1.1629483037.1675392011; _ga_0ZMCE92ST2=GS1.1.1706743280.2.1.1706743308.0.0.0; PortalSID=dab52b091a987584d34d497b543f0de1; PortalLoggedIn=1; device=desktop',
	'Accept': 'application/json, text/plain, */*',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:121.0) Gecko/20100101 Firefox/121.0',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'DNT': '1',
	'Sec-GPC': '1',
	'Connection': 'keep-alive',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-origin',
	'TE': 'trailers'
}

response = get('https://merewether-h.sentral.com.au/s-n2v7Be/portal2/timetable/getFullTimetableInDates/2929/undefined/true', headers=headers)
json = response.json()

fortnight = convertjson(json)

print(fortnight)
