from datetime import datetime
import string
import random

from flask import current_app
from .extensions import db
from .utils import generate_id
from .utils.database import CRUDMixin

class Activity(CRUDMixin, db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    meetup_id = db.Column(db.String(9), db.ForeignKey('meetups.id'))
    tripadvisor_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    votes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Activity %r>' % self.name

class TimeSlot(CRUDMixin, db.Model):
    __tablename__ = 'timeslots'

    id = db.Column(db.Integer, primary_key=True)
    meetup_id = db.Column(db.String(9), db.ForeignKey('meetups.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    votes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<TimeSlot>'

class Meetup(CRUDMixin, db.Model):
    __tablename__ = 'meetups'

    id = db.Column(db.String(9), primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(9))
    organizer = db.Column(db.String(255))

    activities = db.relationship('Activity',
            foreign_keys=[Activity.meetup_id],
            backref=db.backref('meetup', lazy='joined'),
            lazy='dynamic',
            cascade='all, delete-orphan')

    timeslots = db.relationship('TimeSlot',
            foreign_keys=[TimeSlot.meetup_id],
            backref=db.backref('meetup', lazy='joined'),
            lazy='dynamic',
            cascade='all, delete-orphan')

    def __init__(self, **kwargs):
        super(Meetup, self).__init__(**kwargs)
        while True:
            self.id = generate_id()
            if Meetup.query.get(self.id) is None:
                break
        self.password = generate_id()

    def __repr__(self):
        return '<User %r>' % self.name