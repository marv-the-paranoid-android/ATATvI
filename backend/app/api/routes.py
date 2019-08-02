from flask import jsonify
from app.models import Tweets
from app.api import bp


@bp.route('/process/getwork', methods=['GET'])
def process_getwork():
    tweet = Tweets.query.filter_by(status=0).first()
    if tweet is None:
        return jsonify(None)
    return jsonify(tweet)


@bp.route('/process/dowork/<int:id>', methods=['PUT'])
def process_dowork(id):
    return jsonify(None)


@bp.route('/report', methods=['GET'])
def report():
    return jsonify(None)
