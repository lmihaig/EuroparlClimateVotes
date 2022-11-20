import itertools
import io
import requests
import tempfile
import re
import threading
import time
from pprint import pprint
from os import environ
import model
model=model.Model()
import xml.etree.ElementTree as ET

time.sleep(10)

def get_url(day, month, year=2022, lang="FR"):
    return f"https://www.europarl.europa.eu/doceo/document/PV-9-{year}-{month:02}-{day:02}-RCV_{lang}.xml"

# 1 hour
FORCE_TIME_SLEEP=60*60
# 1 day
NEXT_TIME_SLEEP=60*60*24
FORCE_BETWEN_NEXTS=NEXT_TIME_SLEEP/FORCE_TIME_SLEEP
BASE_URL=environ.get("API_BASE_URL", "http://127.0.0.1:5000")
session = requests.Session()

def skip_seq(target, seq, count=1): return target.split(seq, count)[-1]
def take_til_seq(target, seq, count=1): return seq.join(target.split(seq, count)[:-1])
def rskip_seq(target, seq, count=1): return target.rsplit(seq, count)[0]

amendment_pattertn=re.compile("A[0-9]+-[0-9]+\/[0-9]{4}")

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
        description=list(result.iter("RollCallVote.Description.Text"))[0].text

        if not description:
            print("BBBBBBBB")
            continue

        description=description.strip().replace("–", "-").replace("’","'").replace('“', '"').replace('”', '"').replace('\n', ' ')
        if description.count("-")<=1:
            continue

        am=None
        if description.rsplit("-", 1)[1].startswith(" Am "):
            description, am =description.rsplit(" - ", 1)

        if amendment_pattertn.match(description):
            print("CCCCCCCCC", description)
            description=previous_name
            used_previous_name=True
        else:
            if description.count("-")<=1:
                continue

            extra_sep_val=0

            if amendment_pattertn.match(description.rsplit(" - ",3)[1]):
                extra_sep_val=-2
            elif amendment_pattertn.match(description.rsplit(" - ",4)[1]):
                extra_sep_val=-3
            else:
                extra_sep_val=1

            separators=(description.count(description_separator)+extra_sep_val)//3

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
            "address":url.replace(".xml", ".pdf"),
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
    return returned

def check_ml(a):
    return model.predict(a)


resp=session.get(BASE_URL+"/internal/state")
day=resp.json()["day"]
month=resp.json()["month"]
year=resp.json()["year"]

def next_date(day, month, year):
    day+=1

    if day % 32==0:
        day=1
        month+=1

    if month%13==0:
        month=1
        year+=1

    return day, month, year

def next_check():
    global day, month, year
    try_day, try_month, try_year=day, month, year
    for _ in range(90):
        try_day, try_month, try_year=next_date(try_day, try_month, try_year)
        if session.get(get_url(try_day, try_month, try_year)).status_code==200:
            # FOUND
            print("FOUND:", try_day, try_month, try_year)

            climate_votes=extract_votes(get_url(try_day, try_month, try_year))
            for climate_vote in climate_votes:
                print("adding")
                requests.post(BASE_URL+"/internal/vote", json=climate_vote)

            day, month, year=try_day, try_month, try_year
            # save state
            session.post(BASE_URL+"/internal/state", json={
                "day":day,
                "month":month,
                "year":year,
            })
            break
    print("NEXT check: DONE")
# next_check()
# exit()

print(day, month, year)
while True:

    next_check()

    for _ in range(FORCE_BETWEN_NEXTS):

        # DO FORCE_CHECK

        time.sleep(FORCE_TIME_SLEEP)
