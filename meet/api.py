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

api.add_resource(NewMeetup, "/meetups")