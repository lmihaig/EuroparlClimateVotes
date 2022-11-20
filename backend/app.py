from flask import Flask, request
from flask_restx import Resource, Api
from documents import *

app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request_func(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@api.route('/internal/vote')
class vote(Resource):
    def post(self):
        args = request.get_json()
        vote=Vote(
            meps_pro=[
                MEP(**mep) for mep in args["pro"]
            ],
            meps_contra=[
                MEP(**mep) for mep in args["contra"]
            ],
            meps_abstain=[
                MEP(**mep) for mep in args["abstain"]
            ],
            name=args["name"],
            address=args["address"]
        )
        with mongoConnection:
            vote.save()

@api.route('/force/vote')
class ForceVote(Resource):
    def post(self):
        args = request.get_json()
        vote=RequestedVote(
            # TODO
        )
        with mongoConnection:
            vote.save()
    def get(self):
        votes=RequestedVote.objects(consumed==False)
        if len(votes)==0:
            return {
                "job":None
            }

        vote=votes[0]
        vote.consumed=True
        vote.save()
        return {
            "job": vote.address,
            "title": vote.title,
        }
@api.route('/internal/state')
class StateApi(Resource):
    def post(self):
        args = request.get_json()
        with mongoConnection:
            state=State.objects[0]
            state.year=args["year"]
            state.month=args["month"]
            state.day=args["day"]
            state.save()
    def get(self):
        with mongoConnection:
            state=State.objects[0]
        return {
            "year": state.year,
            "month": state.month,
            "day": state.day,
        }


@app.get("/laws")
def get_laws():
    with mongoConnection:
        laws=list(Vote.objects)

    return {"laws":[
        {
            "name": law.name,
            "pro": len(law.meps_pro),
            "contra": len(law.meps_contra),
            "abstain": len(law.meps_abstain),
        } for law in laws
    ]}


@app.get("/meps")
def get_meps():
    with mongoConnection:
        laws=list(Vote.objects)

    def init_mep(name): return {"name":name, "pro":0, "contra":0, "abstain":0}

    meps={}
    for law in laws:
        for mep in law.meps_pro:
            if mep.name not in meps:
                meps[mep.name]=init_mep(mep.name)
            meps[mep.name]["pro"]+=1
        for mep in law.meps_contra:
            if mep.name not in meps:
                meps[mep.name]=init_mep(mep.name)
            meps[mep.name]["contra"]+=1
        for mep in law.meps_abstain:
            if mep.name not in meps:
                meps[mep.name]=init_mep(mep.name)
            meps[mep.name]["abstain"]+=1

    return {
        "meps":sorted(list(meps.values()), key=lambda x:(x["pro"]+x["contra"]+x["abstain"]), reverse=True)
    }


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
