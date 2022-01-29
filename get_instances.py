import requests
import json
from bs4 import BeautifulSoup

mightyList = {}

# Youtube (Invidious)
r = requests.get('https://api.invidious.io/instances.json')
rJson = json.loads(r.text)
invidiousList = []
for instance in rJson:
    invidiousList.append(instance[0])
mightyList["invidious"] = invidiousList


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
        nitterList.append(a.contents[0])
mightyList["nitter"] = nitterList


# Instagram (Bibliogram)
r = requests.get('https://bibliogram.art/api/instances')
rJson = json.loads(r.text)
bibliogramList = []
for instance in rJson["data"]:
    result = instance["address"]
    result = result.replace("https://", "")
    bibliogramList.append(result)
mightyList["bibliogram"] = bibliogramList


# Reddit (Teddit)
r = requests.get(
    'https://codeberg.org/teddit/teddit/raw/branch/main/instances.json')
rJson = json.loads(r.text)
tedditList = []
for item in rJson:
    url = item["url"]
    if url != "":
        url = url.replace("https://", "")
        tedditList.append(url)
mightyList["teddit"] = tedditList


# Wikipedia (Wikiless)
r = requests.get('https://wikiless.org/instances.json')
rJson = json.loads(r.text)
mightyList["wikiless"] = rJson

# Medium (Scribe)
r = requests.get(
    'https://git.sr.ht/~edwardloveall/scribe/blob/main/docs/instances.json')
rJson = json.loads(r.text)
scribeList = []
for item in rJson:
    item = item.replace("https://", "")
    scribeList.append(item)
mightyList["scribe"] = scribeList

# Writing to file
json_object = json.dumps(mightyList, ensure_ascii=False, indent=2)
with open("data.json", "w") as outfile:
    outfile.write(json_object)
print(json_object)
print("Wrote: data.json")
