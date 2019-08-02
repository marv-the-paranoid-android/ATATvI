from datetime import datetime, timedelta
import os


from app import db


class Tweets(db.Model): # @TODO, How do I make the primary unique

    # @TODO:
    # Make unique key (party, person, date)
    # Index Status

    id             = db.Column(db.Integer, primary_key=True) # @TODO, is this auto_increment?
    party          = db.Column(db.String(256), nullable=False)
    person         = db.Column(db.String(256), nullable=False)
    tweet          = db.Column(db.String(280), nullable=False)
    status         = db.Column(db.String(1), default=0, nullable=False)   # @DOC: 0==tobeprocessed, 1==processing, 2==processed
    tone_anger     = db.Column(db.Float)
    tone_fear      = db.Column(db.Float)
    tone_joy       = db.Column(db.Float)
    tone_sadness   = db.Column(db.Float)
    tone_analytic  = db.Column(db.Float)
    tone_confident = db.Column(db.Float)
    tone_tentative = db.Column(db.Float)

    def to_dict(self):
        return {
            "id"             : self.id,
            "party"          : self.party,
            "person"         : self.person,
            "datetime"       : self.datetime,
            "status"         : self.status,
            "tone_anger"     : self.tone_anger,
            "tone_fear"      : self.tone_fear,
            "tone_joy"       : self.tone_joy,
            "tone_sadness"   : self.tone_sadness,
            "tone_analytic"  : self.tone_analytic,
            "tone_confident" : self.tone_confident,
            "tone_tentative" : self.tone_tentative

        }

