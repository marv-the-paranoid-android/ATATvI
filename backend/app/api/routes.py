from flask import jsonify, request, url_for, g, abort
from app import db
from app.models import Tweets
from app.api import bp


@bp.route('/process/getwork', methods=['GET'])
def process_getwork():
    return jsonify(None)

@bp.route('/process/dowork/<int:id>', methods=['PUT'])
def process_dowork(id):
    return jsonify(None)

@bp.route('/report', methods=['GET'])
def report():
    return jsonify(None)




from app.models import Tweets  # noqa: E402

