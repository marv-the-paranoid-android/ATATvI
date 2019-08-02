from app import db


# noqa: E203
# noqa: E221

class Tweets(db.Model):

    # @TODO:
    # Index Status

    # noqa: are added to ignore lining up these columns
    # which I think is important right now, during dev

    id             = db.Column(db.Integer, primary_key=True)        # @TODO, is this auto_increment?
    party          = db.Column(db.String(256), nullable=False)      # noqa: E221
    person         = db.Column(db.String(256), nullable=False)      # noqa: E221
    tweet          = db.Column(db.String(280), nullable=False)      # noqa: E221
    status         = db.Column(db.String(1), default=0, nullable=False) # noqa:501 @DOC: 0==tobeprocessed, 1==processing, 2==processed
    tone_anger     = db.Column(db.Float)
    tone_fear      = db.Column(db.Float)
    tone_joy       = db.Column(db.Float)
    tone_sadness   = db.Column(db.Float)
    tone_analytic  = db.Column(db.Float)
    tone_confident = db.Column(db.Float)
    tone_tentative = db.Column(db.Float)

    def to_dict(self):
        return {
            "id"             : self.id,              # noqa: E203
            "party"          : self.party,           # noqa: E203
            "person"         : self.person,          # noqa: E203
            "datetime"       : self.datetime,        # noqa: E203
            "status"         : self.status,          # noqa: E203
            "tone_anger"     : self.tone_anger,      # noqa: E203
            "tone_fear"      : self.tone_fear,       # noqa: E203
            "tone_joy"       : self.tone_joy,        # noqa: E203
            "tone_sadness"   : self.tone_sadness,    # noqa: E203
            "tone_analytic"  : self.tone_analytic,   # noqa: E203
            "tone_confident" : self.tone_confident,  # noqa: E203
            "tone_tentative" : self.tone_tentative   # noqa: E203

        }
