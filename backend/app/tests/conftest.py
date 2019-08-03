import pytest
from app import create_app, db
from config import Config
from app.models import Tweet


class TestConfig(Config):
    # in memory database for testing
    SQLALCHEMY_DATABASE_URI = "sqlite://"


@pytest.fixture
def client():

    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    with app.test_client() as client:
        yield client

    db.session.remove()
    db.drop_all()
    app_context.pop()


@pytest.fixture
def sample_tweet(client):
    tweet = Tweet(party="GOP", person="Trump", tweet="Bigly")
    db.session.add(tweet)
    db.session.commit()
    return tweet
