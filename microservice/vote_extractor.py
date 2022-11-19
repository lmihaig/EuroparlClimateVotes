import io
import requests
import tempfile
import re
import threading
from pprint import pprint
import xml.etree.ElementTree as ET
def get_url(day, month, lang="FR"):
    return f"https://www.europarl.europa.eu/doceo/document/PV-9-2022-{month:02}-{day:02}-RCV_{lang}.xml"

session = requests.Session()

def skip_seq(target, seq, count=1): return target.split(seq, count)[-1]
def take_til_seq(target, seq, count=1): return seq.join(target.split(seq, count)[:-1])
def rskip_seq(target, seq, count=1): return target.rsplit(seq, count)[0]

amendment_pattertn=re.compile("A[0-9]+-[0-9]+\/[0-9]{4}")

def extract_names(url):
    resp=session.get(url)
    if resp.status_code != 200:
        if resp.status_code != 404:
            print(resp)
        return []

    tree = ET.parse(io.StringIO(resp.text))
    root = tree.getroot()
    description_separator=" - "
    returned=[]
    for result in root.iter("RollCallVote.Result"):
        description=list(result.iter("RollCallVote.Description.Text"))[0]
        description=description.text
        if not description:
            continue
        if amendment_pattertn.match(description):
            continue
        # print(description)
        # continue
        description=description.strip().replace("–", "-").replace("’","'").replace('“', '"').replace('”', '"')
        am=None
        if description.rsplit("-", 1)[1].startswith(" Am "):
            # print("AAAA")
            description, am =description.rsplit(" - ", 1)
        # print(description)
        extra_sep_val=0
        # print(description.rsplit(" - ",3)[1])
        if amendment_pattertn.match(description.rsplit(" - ",3)[1]):
            extra_sep_val=-2
        elif amendment_pattertn.match(description.rsplit(" - ",4)[1]):
            extra_sep_val=-3
        else:
            extra_sep_val=1
        separators=(description.count(description_separator)+extra_sep_val)//3
        # print(description.count(description_separator), separators, "#", extra_sep_val)
        if separators <=0:
            continue
        description=take_til_seq(skip_seq(description,
            description_separator, separators),
            description_separator, separators
        )
        returned.append(description)
        # print(description)
        # exit()
    return returned


# for day in range(1,31):
#     for month in range(7,10):
#         resp=requests.get(get_url(day, month))
#         # print(resp)
#         if resp.status_code ==200:
#             print(day, month)

# a=extract_names(get_url(15, 9))
# a=extract_names(get_url(13, 9))
# a=extract_names(get_url(5, 7))
# a=extract_names(get_url(4, 7))
# pprint(a)
# exit()



output="nume,\n"

def scan_month(month, year):
    global output
    for day in range(1,32):
        for name in extract_names(get_url(day, month)):
            # print(name)
            output+=f"{name},\n"

months=[]
for year in range(2015, 2023):
    for month in range(1, 13):
        thread=threading.Thread(target=scan_month, args=(month, year,))
        thread.start()
        months.append(thread)

list(map(threading.Thread.join, months))

with open("train.csv", "w") as f:
    f.write(output)
