# -*- coding: utf-8 -*-

from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_number = db.Column(db.String(64))
    name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    passport_number = db.Column(db.String(64))
    delivery_needed = db.Column(db.Boolean)
    sex = db.Column(db.String(7))
    address = db.Column(db.String(40))
    citizenship = db.Column(db.Integer)
    birth_date = db.Column(db.Date)
    entry_date = db.Column(db.Date)
    exit_date = db.Column(db.Date)
    kids = db.Column(db.String(64))
    transport = db.Column(db.String(64))
    email = db.Column(db.String(64))
    cities = db.Column(db.String(64))
    if_double = db.Column(db.Boolean)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return 'Person %r' % self.name
