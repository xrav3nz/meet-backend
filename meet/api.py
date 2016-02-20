from datetime import datetime

from flask import request, Blueprint
from flask_restful import Resource, abort

from .models import Meetup, TimeSlot, Activity
from .extensions import api

api_bp = Blueprint('api_bp', __name__)
api.init_app(api_bp)

class NewMeetup(Resource):
    def post(self):
        data = request.get_json(force=True)
        meetup = Meetup(name=data['name'], organizer=data['organizer'])
        meetup.save()

        for ts in data['timeslots']:
            timeslot = TimeSlot(meetup_id=meetup.id)
            timeslot.start_time = datetime.strptime(ts['start_time'], '%Y-%m-%d %H:%M:%S')
            timeslot.end_time = datetime.strptime(ts['end_time'], '%Y-%m-%d %H:%M:%S')
            timeslot.save()

        for ac in data['activities']:
            activity = Activity(meetup_id=meetup.id)
            activity.tripadvisor_id = ac['tripadvisor_id']
            activity.name = ac['name']
            activity.save()

        return {
                'id': meetup.id,
                'password': meetup.password
                }, 200

class Meetups(Resource):
    def get(self, meetup_id):
        meetup = Meetup.query.get_or_404(meetup_id)
        meetup.timeslots.all()
        meetup.activities.all()

        timeslots = []
        for ts in meetup.timeslots:
            timeslots.append({
                    'start_time': str(ts.start_time),
                    'end_time': str(ts.end_time),
                    'votes': ts.votes
                })

        activities = []
        for ac in meetup.activities:
            activities.append({
                    'tripadvisor_id': ac.tripadvisor_id,
                    'name': ac.name,
                    'votes': ac.votes
                })

        return {
                'id': meetup.id,
                'name': meetup.name,
                'organizer': meetup.organizer,
                'timeslots': timeslots,
                'activities': activities
        }


api.add_resource(NewMeetup, "/meetups")
api.add_resource(Meetups, "/meetups/<string:meetup_id>")