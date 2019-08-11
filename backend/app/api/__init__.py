from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import routes  # noqa: 401  .. we have to do this
