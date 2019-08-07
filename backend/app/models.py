from app import db

# **** NOTE: Why are all these #noqa: E??? comments here??
# noqa: E203
# noqa: E221
#
# Ya, I know. I like lined up code and was hoping we could
# leave these here until the data model is locked down.
# IMHO, it makes it easier to read


class Processed(db.Model):
    person = db.Column(db.String(256), primary_key=True, nullable=False)
    numprocessed = db.Column(db.Integer, default=0)

    def __init__(self, person, numprocessed=0):
        super().__init__()
        self.person = person
        self.numprocessed = numprocessed

    def to_dict(self):
        return {
            "person": self.person,
            "numprocessed": self.numprocessed
        }


class Tweet(db.Model):

    # @TODO:
    # Index Status

    # noqa: are added to ignore lining up these columns
    # which I think is important right now, during dev

    id             = db.Column(db.Integer, primary_key=True)        # noqa: E221 E501 @TODO, is this auto_increment?
    party          = db.Column(db.String(256), nullable=False)      # noqa: E221 E501
    person         = db.Column(db.String(256), nullable=False)      # noqa: E221 E501
    tweet          = db.Column(db.String(280), nullable=False)      # noqa: E221 E501
    status         = db.Column(db.String(1), default=0, nullable=False) # noqa:501 @DOC: 0==tobeprocessed, 1==processing, 2==processed
    tone_anger     = db.Column(db.Float, default=0)  # noqa: E221
    tone_fear      = db.Column(db.Float, default=0)  # noqa: E221
    tone_joy       = db.Column(db.Float, default=0)  # noqa: E221
    tone_sadness   = db.Column(db.Float, default=0)  # noqa: E221
    tone_analytic  = db.Column(db.Float, default=0)  # noqa: E221
    tone_confident = db.Column(db.Float, default=0)
    tone_tentative = db.Column(db.Float, default=0)

    def __init__(self, party, person, tweet):
        super().__init__()

        self.party  = party  # noqa: E221
        self.person = person
        self.tweet  = tweet  # noqa: E221

    def to_dict(self):
        return {
            "id"             : self.id,              # noqa: E203
            "party"          : self.party,           # noqa: E203
            "person"         : self.person,          # noqa: E203
            "tweet"          : self.tweet,           # noqa: E203
            "status"         : self.status,          # noqa: E203
            "tone_anger"     : self.tone_anger,      # noqa: E203
            "tone_fear"      : self.tone_fear,       # noqa: E203
            "tone_joy"       : self.tone_joy,        # noqa: E203
            "tone_sadness"   : self.tone_sadness,    # noqa: E203
            "tone_analytic"  : self.tone_analytic,   # noqa: E203
            "tone_confident" : self.tone_confident,  # noqa: E203
            "tone_tentative" : self.tone_tentative   # noqa: E203
        }
