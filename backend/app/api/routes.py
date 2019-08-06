from flask import jsonify, request
from app import db
from app.models import Tweet
from app.api import bp
from app.api.errors import bad_request
from app.components.watson import Watson
import json


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
        party=data.get("party"),
        person=data.get("person"),
        tweet=data.get("tweet")
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
    # @REVIST: Honestly, this probably shouldn't be exposed,
    # as it's really only used for internal processing. But
    # it's here
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
    tweet = Tweet.query.get(id)
    if not tweet or tweet.status == 0:  # @TODO turn status into EnumInt
        return bad_request(f'tweet::id:[{id}] is not a valid status for processing.')  # noqa: E501

    # Set Status to in Progress
    tweet.status = 1
    db.session.add(tweet)
    db.session.commit()

    # Send Payload to Watson
    # @TODO Send Payload
    watson = Watson(tweet.tweet, 'watson-return.txt')
    data = watson.getMock('document_tone')

    # Save Payload from Watson
    success = False
    payload = json.loads(data.response[0])
    # payload:[{'document_tone': {'tones': [{'score': 0.766478, 'tone_id': 'sadness', 'tone_name': 'Sadness'}]}}]   # noqa: E501

    if 'tones' in payload['document_tone']:
        for rec in payload['document_tone']['tones']:
            # rec:[{'score': 0.766478, 'tone_id': 'sadness', 'tone_name': 'Sadness'}]  # noqa: E501
            if 'tone_id' in rec:
                tone_id = 'tone_' + rec['tone_id']
                setattr(tweet, tone_id, rec['score'])
                success = True

    # Set Status to Complete
    if success:
        tweet.status = 2
    else:
        tweet.status = 99
    db.session.add(tweet)
    db.session.commit()

    return jsonify(tweet.to_dict())


@bp.route('/report', methods=['GET'])
def report():
    data = {
        "parties": [
            {
                "party"     : "GOP",  # noqa: E203
                "anger"     : 0.75,   # noqa: E203
                "fear"      : 0.69,   # noqa: E203
                "joy"       : 0.00,   # noqa: E203
                "sadness"   : 0.88,   # noqa: E203
                "analytic"  : 0.10,   # noqa: E203
                "confident" : 0.51,   # noqa: E203
                "tentative" : 0.22    # noqa: E203
            },
            {
                "party"     : "DEM",  # noqa: E203
                "anger"     : 0.10,   # noqa: E203
                "fear"      : 0.11,   # noqa: E203
                "joy"       : 0.70,   # noqa: E203
                "sadness"   : 0.51,   # noqa: E203
                "analytic"  : 0.52,   # noqa: E203
                "confident" : 0.49,   # noqa: E203
                "tentative" : 0.53    # noqa: E203
            }
        ]
    }
    return jsonify(data)
