import urllib.error, urllib.request, urllib.parse
import json


target='http://py4e-data.dr-chuck.net/json?'
local=input('Location---')
url=target+urllib.parse.urlencode({'address':local, 'key':42})



print('Retriving.....',url)
data=urllib.request.urlopen(url).read()
print('Retrived..',len(data),'characters')
js=json.loads(data)
print(json.dumps(js,indent=4))
print('Place ID->',js['results'][0]['place_id'])
