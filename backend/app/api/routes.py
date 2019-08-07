from flask import jsonify, request, Response
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
        return bad_request('No records to process.')
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

    # I can't get these to work!!!
    # Always, my response.data is blank
    # this is all the result of trying to change the status
    # code to 204, so I'm not going to. But I'm going to leave these here
    # for later
    #
    # **** TRY #1
    # this is different, in that we are creating a Response() object
    # directly, note the use of json.dumps() against the .to_dict()
    # response = Response(
    #     response=json.dumps(tweet.to_dict()),
    #     status=204,
    #     content_type='application/json'
    # )
    # return response
    #
    # **** TRY #2
    # response = app.response_class(response=json.dumps({"name":"avalue"}),
    #                               status=204,
    #                               mimetype='application/json')
    # return response
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

# @bp.route('/tweets/anger', methods=['GET'])
# def get_all_angry_tweets():
#     tweets = [tweet.to_dict() for tweet in Tweet.query.filter(Tweet.tone_anger >= 0.4)]
#     return jsonify(tweets)
    
# @bp.route('tweets/fear', methods=['GET'])
# def get_all_fear_tweets():
#     tweets = [tweet.to_dict() for tweet in Tweet.query.filter(Tweet.tone_fear >= 0.4)]
#     return jsonify(tweets)

# @bp.route('tweets/joy', methods=['GET'])
# def get_all_joy_tweets():
#     tweets = [tweet.to_dict() for tweet in Tweet.query.filter(Tweet.tone_joy >= 0.4)]
#     return jsonify(tweets)

# @bp.route('tweets/sadness', methods=['GET'])
# def get_all_sadness_tweets():
#     tweets = [tweet.to_dict() for tweet in Tweet.query.filter(Tweet.tone_sadness >= 0.4)]
#     return jsonify(tweets)

# @bp.route('tweets/analytic', methods=['GET'])
# def get_all_analytic_tweets():
#     tweets = [tweet.to_dict() for tweet in Tweet.query.filter(Tweet.tone_analytic >= 0.4)]
#     return jsonify(tweets)

# @bp.route('tweets/confident', methods=['GET'])
# def get_all_confident_tweets():
#     tweets = [tweet.to_dict() for tweet in Tweet.query.filter(Tweet.tone_confident >= 0.4)]
#     return jsonify(tweets)

# @bp.route('tweets/tentative', methods=['GET'])
# def get_all_tentative_tweets():
#     tweets = [tweet.to_dict() for tweet in Tweet.query.filter(Tweet.tone_tentative >= 0.4)]
#     return jsonify(tweets)

@bp.route('tweets/<string:tone>', methods=['GET'])
def get_all_tone_tweets(tone):
    query_param = request.url.split('/')[-1]
    tweets = str([tweet.to_dict() for tweet in Tweet.query.filter(getattr(Tweet, query_param) >= 0.4)])
    print(tweets.split('person')[1].split('tweet')[0].split("'")[2])
    print(tweets.split('person')[1].split('tweet')[1].split("'")[2])
    return tweets