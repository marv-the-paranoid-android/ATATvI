import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = 'djskjdi3j2jdwkndwkjdwkjd'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
        or 'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ECHO = False
