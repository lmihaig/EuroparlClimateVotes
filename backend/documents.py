from threading import Lock
from mongoengine import Document, EmbeddedDocument, disconnect, connect
from mongoengine.fields import StringField,EmbeddedDocumentListField, URLField, ListField, BooleanField, IntField, DateTimeField, ReferenceField
from datetime import datetime
from os import environ
from ipaddress import ip_address, ip_network
import socket, struct

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

__all__=[
    "mongoConnection",
    "MEP",
    "Vote",
    "State",
]

class MongoConnection(object):
    db_name="ep_watchdog"
    def __init__(self):
        self.lock = Lock()
        self.connection=None
    def __enter__(self):
        self.lock.acquire()
        self.connection=connect(
            __class__.db_name,
            username=environ.get("MONGO_USER", None),
            password=environ.get("MONGO_PASSWORD", None),
            host=environ.get("MONGO_HOST", "192.168.0.210"),
        )
    def __exit__(self, type, value, traceback):
        disconnect(__class__.db_name)
        self.lock.release()

mongoConnection=MongoConnection()


class MEP(EmbeddedDocument):
    # nume
    name=StringField(required=True)
    # partid (NU ca se schimba)
    party=StringField()

    meta={"indexes": [
        {"fields": ["name",]},
        {"fields": ["party",]},
    ]}



class Vote(Document):
    state=StringField(default="added", choices=["added", "verified"])

    # climateIdeal
    # AFTER verified
    climateIdeal=StringField(choices=["pro","contra"])

    # parlamentars(+vote)
    meps_pro=EmbeddedDocumentListField(MEP, required=True)
    meps_contra=EmbeddedDocumentListField(MEP, required=True)
    meps_abstain=EmbeddedDocumentListField(MEP, required=True)

    # name
    name=StringField(required=True)

    # description
    # AFTER verified
    description=StringField()

    # date=DateTimeField(required=True)
    address=URLField(required=True)

    meta={"indexes": [
        {"fields": ["state",]},
        {"fields": ["name",]},
    ]}

class RequestedVote(Document):
    address=URLField(required=True)
    title=StringField(required=True)

    consumed=BooleanField(default=False)

    meta={"indexes": [
        {"fields": ["consumed",]},
    ]}

class State(Document):
    year=IntField(default=2022)
    month=IntField(default=11)
    day=IntField(default=10)

# init state
with mongoConnection:
    if len(State.objects)==0:
        State().save()

if __name__ == '__main__':
    exit()
    with mongoConnection:
        v=Vote(
            climateIdeal="pro",
            meps=[
                MEP(name="Gigi")
            ],
            name="Test",
            address="https://sima.zapto.org"
        )
        v.save()
    a=list(Vote.objects)[0]
    print(a.to_json())
