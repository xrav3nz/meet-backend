from flask_restful import reqparse, abort, Resource

class NewMeetup(Resource):
    def post(self):
        return {'hello': 'world'}