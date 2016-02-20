from datetime import datetime
from flask import current_app
from ..extensions import db
from ..utils.database import CRUDMixin

class Activity(CRUDMixin, db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    meetup_id = db.Column(db.Integer, db.ForeignKey('meetups.id'))
    tripadvisor_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    votes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Activity %r>' % self.name

class TimeSlot(CRUDMixin, db.Model):
    __tablename__ = 'timeslots'

    id = db.Column(db.Integer, primary_key=True)
    meetup_id = db.Column(db.Integer, db.ForeignKey('meetups.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.Datetime)
    votes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<TimeSlot>'

class Meetup(CRUDMixin, db.Model):
    __tablename__ = 'meetups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
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

    def __repr__(self):
        return '<User %r>' % self.username