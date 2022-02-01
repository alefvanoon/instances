import requests
import json
from urllib.parse import urlparse
from bs4 import BeautifulSoup

mightyList = {}


def get_host_name(link):
    url = urlparse(link)
    return url.netloc


# Invidious
r = requests.get('https://api.invidious.io/instances.json')
rJson = json.loads(r.text)
invidiousList = []
for instance in rJson:
    invidiousList.append(instance[0])
mightyList["invidious"] = invidiousList
print("Wrote Invidious")


# Nitter
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
print("Wrote Nitter")

# Bibliogram
r = requests.get('https://bibliogram.art/api/instances')
rJson = json.loads(r.text)
bibliogramList = []
for item in rJson["data"]:
    hostname = get_host_name(item["address"])
    bibliogramList.append(hostname)
mightyList["bibliogram"] = bibliogramList
print("Wrote Bibliogram")


# Teddit
r = requests.get(
    'https://codeberg.org/teddit/teddit/raw/branch/main/instances.json')
rJson = json.loads(r.text)
tedditList = []
for item in rJson:
    url = item["url"]
    if url != "":
        tedditList.append(get_host_name(url))
mightyList["teddit"] = tedditList
print("Wrote Teddit")


# Wikiless
r = requests.get('https://wikiless.org/instances.json')
rJson = json.loads(r.text)
mightyList["wikiless"] = rJson
print("Wrote Wikiless")


# Scribe
r = requests.get(
    'https://git.sr.ht/~edwardloveall/scribe/blob/main/docs/instances.json')
rJson = json.loads(r.text)
scribeList = []
for item in rJson:
    scribeList.append(get_host_name(item))
mightyList["scribe"] = scribeList
print("Wrote Scribe")


# SimplyTranslate
r = requests.get('https://simple-web.org/instances/simplytranslate')
simplyTranslateList = r.text.strip().split("\n")
mightyList["simplyTranslate"] = simplyTranslateList
print("Wrote SimplyTranslate")


# SearX
r = requests.get('https://searx.space/data/instances.json')
rJson = json.loads(r.text)
searxList = []
for instanceLink in rJson["instances"].keys():
    url = urlparse(instanceLink)
    searxList.append(url.netloc)
mightyList["searx"] = searxList
print("Wrote SearX")


# Whoogle
r = requests.get(
    'https://raw.githubusercontent.com/benbusby/whoogle-search/main/misc/instances.txt')
tmpList = r.text.strip().split("\n")
whoogleList = []
for instanceLink in tmpList:
    url = urlparse(instanceLink)
    whoogleList.append(url.netloc)
mightyList["whoogle"] = whoogleList
print("Wrote Whoogle")


# Writing to file
json_object = json.dumps(mightyList, ensure_ascii=False, indent=2)
with open("data.json", "w") as outfile:
    outfile.write(json_object)
# print(json_object)
print("Wrote: data.json")
