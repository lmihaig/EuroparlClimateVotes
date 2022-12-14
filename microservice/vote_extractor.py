import itertools
import io
import requests
import tempfile
import re
import threading
from pprint import pprint
import xml.etree.ElementTree as ET
def get_url(day, month, year=2022, lang="FR"):
    return f"https://www.europarl.europa.eu/doceo/document/PV-9-{year}-{month:02}-{day:02}-RCV_{lang}.xml"

session = requests.Session()

def skip_seq(target, seq, count=1): return target.split(seq, count)[-1]
def take_til_seq(target, seq, count=1): return seq.join(target.split(seq, count)[:-1])
def rskip_seq(target, seq, count=1): return target.rsplit(seq, count)[0]

amendment_pattertn=re.compile("A[0-9]+-[0-9]+\/[0-9]{4}")

def extract_names(url, *, session=session):
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
        description=description.strip().replace("–", "-").replace("’","'").replace('“', '"').replace('”', '"').replace('\n', ' ')
        if description.count("-")<=1:
            continue
        am=None
        if description.rsplit("-", 1)[1].startswith(" Am "):
            description, am =description.rsplit(" - ", 1)
            # print("AAAA", am)
        # print(description)
        if description.count("-")<=1:
            continue
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
        # if am:
        #     print(description,"#", am)
        returned.append(description)
        # print(description)
        # exit()
    return returned

def extract_votes(url, *, session=session):
    resp=session.get(url)
    global previous_name
    used_previous_name=False
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
            print("BBBBBBBB")
            continue
        # print(description)
        # continue
        description=description.strip().replace("–", "-").replace("’","'").replace('“', '"').replace('”', '"').replace('\n', ' ')
        if description.count("-")<=1:
            continue
        am=None
        if description.rsplit("-", 1)[1].startswith(" Am "):
            description, am =description.rsplit(" - ", 1)
            # print("AAAA", am)
        # print(description)
        if amendment_pattertn.match(description):
            print("CCCCCCCCC", description)
            description=previous_name
            used_previous_name=True
        else:
            if description.count("-")<=1:
                continue
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

        if not used_previous_name:
            previous_name=description

        resultFor=next(result.iter("Result.For"))
        resultAgainst=next(result.iter("Result.Against"))
        resultAbstention=next(result.iter("Result.Abstention"))

        if not check_ml(description):
            continue

        if am:
            print(description,"#", am)
            description+=" "+am
        returned.append({
            "address":url,
            "name":description,
            "pro": list(itertools.chain.from_iterable([[
                    {
                        "name":mep.text,
                        "party": partyNode.get("Identifier"),
                    } for mep in partyNode.iter("PoliticalGroup.Member.Name")
                ] for partyNode in resultFor.iter("Result.PoliticalGroup.List")
            ])),
            "contra": list(itertools.chain.from_iterable([[
                    {
                        "name":mep.text,
                        "party": partyNode.get("Identifier"),
                    } for mep in partyNode.iter("PoliticalGroup.Member.Name")
                ] for partyNode in resultAgainst.iter("Result.PoliticalGroup.List")
            ])),
            "abstain": list(itertools.chain.from_iterable([[
                    {
                        "name":mep.text,
                        "party": partyNode.get("Identifier"),
                    } for mep in partyNode.iter("PoliticalGroup.Member.Name")
                ] for partyNode in resultAbstention.iter("Result.PoliticalGroup.List")
            ])),
        })
        # print(description)
        # exit()
    return returned

def check_ml(a):
    return True
# for day in range(1,31):
#     for month in range(7,10):
#         resp=requests.get(get_url(day, month))
#         # print(resp)
#         if resp.status_code ==200:
#             print(day, month)

# print(get_url(15, 9))
# a=extract_names(get_url(15, 9))
a=extract_votes(get_url(13, 9))
# a=extract_names(get_url(5, 7))
# a=extract_names(get_url(4, 7))
# a=extract_names(get_url(19, 10, 2021))
for e in a:
    requests.post("http://127.0.0.1:5000/internal/vote", json=e)
# pprint(a)
exit()


output_lock=threading.Lock()
output="nume,\n"

def scan_month(month, year):
    global output
    session = requests.Session()
    local_output=f""
    for day in range(1,32):
        for name in extract_names(get_url(day, month, year), session=session):
            print(day, name)
            name=name.replace("\"", "'")
            local_output+=f"\"{name}\",\n"
    with output_lock:
        output+=local_output

months=[]
# for year in range(2021, 2022):
# year=2022
# for month in range(1, 13):
#     thread=threading.Thread(target=scan_month, args=(month, year,))
#     thread.start()
#     months.append(thread)

# scan_month(10, 2021)

list(map(threading.Thread.join, months))

with open("train.csv", "w") as f:
    f.write(output)
