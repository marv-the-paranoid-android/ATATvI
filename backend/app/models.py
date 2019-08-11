from app import db


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

    # @TODO:Index Status

    id = db.Column(db.Integer, primary_key=True)
    party = db.Column(db.String(256), nullable=False)
    person = db.Column(db.String(256), nullable=False)
    tweet = db.Column(db.String(280), nullable=False)
    status = db.Column(db.String(1), default=0, nullable=False) # noqa:501 @DOC: 0==tobeprocessed, 1==processing, 2==processed
    tone_anger = db.Column(db.Float, default=0)
    tone_fear = db.Column(db.Float, default=0)
    tone_joy = db.Column(db.Float, default=0)
    tone_sadness = db.Column(db.Float, default=0)
    tone_analytic = db.Column(db.Float, default=0)
    tone_confident = db.Column(db.Float, default=0)
    tone_tentative = db.Column(db.Float, default=0)

    def __init__(self, party, person, tweet, tone=None):
        super().__init__()

        self.party = party
        self.person = person
        self.tweet = tweet
        self.tone = tone

    def to_dict(self):
        return {
            "id": self.id,
            "party": self.party,
            "person": self.person,
            "tweet": self.tweet,
            "status": self.status,
            "tone_anger": self.tone_anger,
            "tone_fear": self.tone_fear,
            "tone_joy": self.tone_joy,
            "tone_sadness": self.tone_sadness,
            "tone_analytic": self.tone_analytic,
            "tone_confident": self.tone_confident,
            "tone_tentative": self.tone_tentative
        }
