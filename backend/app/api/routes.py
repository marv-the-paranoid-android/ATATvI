from flask import jsonify, request, url_for, g, abort
from app import db
from app.models import User
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@bp.route('/process/getwork', methods=['GET'])
def process_getwork():
    return jsonify(None)

@bp.route('/process/dowork/<int:id>', methods['PUT'])
def process_dowork(id)
    return jsonify(None)

@bp.route('/report', methods['GET'])
def report()
    return jsonify(None)




from app.models import Boat, Crew  # noqa: E402

