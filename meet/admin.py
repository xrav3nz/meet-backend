from flask import Blueprint
from flask_admin.contrib.sqla import ModelView

from .extensions import admin, db
from .models import Meetup, Activity, TimeSlot

admin_bp = Blueprint('admin_bp', __name__)

admin.add_view(ModelView(Meetup, db.session))
admin.add_view(ModelView(Activity, db.session))
admin.add_view(ModelView(TimeSlot, db.session))