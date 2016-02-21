from datetime import datetime

from flask import request, Blueprint, current_app
from flask_restful import Resource, abort

import requests

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
                }, 201

class Meetups(Resource):
    def get(self, meetup_id):
        meetup = Meetup.query.get_or_404(meetup_id)
        meetup.timeslots.all()
        meetup.activities.all()

        timeslots = []
        for ts in meetup.timeslots:
            timeslots.append({
                    'id': ts.id,
                    'start_time': str(ts.start_time),
                    'end_time': str(ts.end_time),
                    'votes': ts.votes
                })

        activities = []
        for ac in meetup.activities:
            activities.append({
                    'id': ac.id,
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
        }, 200

    def put(self, meetup_id):
        meetup = Meetup.query.get_or_404(meetup_id)
        data = request.get_json(force=True)

        meetup.timeslots.all()
        meetup.activities.all()

        for id in data['timeslot_ids']:
            for ts in meetup.timeslots:
                if ts.id == id:
                    ts.votes += 1
                    ts.save()

        for id in data['activity_ids']:
            for ac in meetup.activities:
                if ac.id == id:
                    ac.votes += 1
                    ac.save()

        timeslots = []
        for ts in meetup.timeslots:
            timeslots.append({
                    'id': ts.id,
                    'votes': ts.votes
                })

        activities = []
        for ac in meetup.activities:
            activities.append({
                    'id': ac.id,
                    'votes': ac.votes
                })

        return {
                'timeslots': timeslots,
                'activities': activities
        }, 200

class Resturants(Resource):
    def get(self, latitude, longitude):
        count = request.args.get('count', 5, type=int)
        url = "http://api.tripadvisor.com/api/partner/2.0/map/%s,%s/restaurants?key=%s" % (latitude, longitude, current_app.config['TA_API_KEY'])
        r = requests.get(url).json()

        results = []

        for data in r['data'][:count]:
            results.append({
                    'web_url': data['web_url'],
                    'name': data['name']
                })

        return {'results': results}, 200


api.add_resource(NewMeetup, "/meetups")
api.add_resource(Meetups, "/meetups/<string:meetup_id>")
api.add_resource(Resturants, "/resturants/<string:latitude>,<string:longitude>")