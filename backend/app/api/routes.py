from flask import jsonify, request
from app import db
from app.models import Tweet
from app.api import bp
from app.api.errors import bad_request


@bp.route('/tweets', methods=['GET'])
def tweet_getall():
    print(f'all:[{Tweet.query.all()}]')
    tweets = [tweet.to_dict() for tweet in Tweet.query.all()]
    return jsonify(tweets)


@bp.route('/tweet/<int:id>', methods=['GET'])
def tweet_getone(id):
    tweet = Tweet.query.get(id)
    return jsonify(tweet.to_dict())


@bp.route('/tweet/create', methods=['POST'])
def tweet_create():
    data = request.json or request.form
    if 'party' not in data or 'person' not in data or 'tweet' not in data:
        return bad_request('must include party & person & tweet')
    tweet = Tweet(
        party=data.get("party"), person=data.get("person"), tweet=data.get("tweet")
    )
    db.session.add(tweet)
    db.session.commit()
    return jsonify(tweet.to_dict())


@bp.route('/process/getpending', methods=['GET'])
def getpending():
    tweet = Tweet.query.filter_by(status=0).first()
    if tweet is None:
        return jsonify(None)  # @TODO send error
    return jsonify(tweet.to_dict())


@bp.route('/process/setstatus/<int:id>', methods=['PUT'])
def process_setstatus(id):
    data = request.get_json() or request.form
    if 'statusid' not in data:
        return bad_request('must include statusid')
    tweet = Tweet.query.filter_by(id=id).first()
    if tweet is None:
        return jsonify(None)  # @TODO send error
    tweet.status = data['statusid']
    db.session.add(tweet)
    db.session.commit()
    response = jsonify(tweet.to_dict())
    response.status_code = 204  # 204=="resource updated successfully"
    #  print(f'status_code:[{response.status_code}]')
    return jsonify(tweet.to_dict())


@bp.route('/process/dowork/<int:id>', methods=['PUT'])
def process_dowork(id):
    return jsonify(None)


@bp.route('/report', methods=['GET'])
def report():
    data = {
        "parties": [
            {
                "party"     : "GOP",
                "anger"     : 0.75,
                "fear"      : 0.69,
                "joy"       : 0.00,
                "sadness"   : 0.88,
                "analytic"  : 0.10,
                "confident" : 0.51,
                "tentative" : 0.22
            },
            {
                "party"     : "DEM",
                "anger"     : 0.10,
                "fear"      : 0.11,
                "joy"       : 0.70,
                "sadness"   : 0.51,
                "analytic"  : 0.52,
                "confident" : 0.49,
                "tentative" : 0.53
            }
        ]
    }
    return jsonify(data)
