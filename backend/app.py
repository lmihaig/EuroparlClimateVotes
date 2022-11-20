from flask import Flask, request
from flask_restx import Resource, Api
from documents import *

app = Flask(__name__)
api = Api(app)

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


if __name__ == '__main__':
    app.run(debug=True)
