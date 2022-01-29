import requests
import json
from bs4 import BeautifulSoup

mightyList = {}

# Youtube (Invidious)
r = requests.get('https://api.invidious.io/instances.json')
rJson = json.loads(r.text)
invidiousList = []
for instance in rJson:
    if instance[0].endswith(".onion"):
        invidiousList.append("http://"+instance[0])
    else:
        invidiousList.append("https://"+instance[0])
mightyList["youtube"] = invidiousList


# Twitter (Nitter)
r = requests.get('https://github.com/zedeus/nitter/wiki/Instances')
soup = BeautifulSoup(r.text, 'html.parser')
markdownBody = soup.find(class_="markdown-body")
tables = markdownBody.find_all("table")
tables.pop(3)
tables.pop(3)
nitterList = []
for table in tables:
    tbody = table.find("tbody")
    trs = tbody.find_all("tr")
    for tr in trs:
        td = tr.find("td")
        a = td.find("a")
        if a.contents[0].endswith(".onion"):
            nitterList.append("http://"+a.contents[0])
        else:
            nitterList.append("https://"+a.contents[0])
mightyList["twitter"] = nitterList


# Instagram (Bibliogram)
r = requests.get('https://bibliogram.art/api/instances')
rJson = json.loads(r.text)
bibliogramList = []
for instance in rJson["data"]:
    bibliogramList.append(instance["address"])
mightyList["instagram"] = bibliogramList


# Writing to file
json_object = json.dumps(mightyList, ensure_ascii=False, indent=2)
with open("data.json", "w") as outfile:
    outfile.write(json_object)
print(json_object)
print("Wrote: data.json")
