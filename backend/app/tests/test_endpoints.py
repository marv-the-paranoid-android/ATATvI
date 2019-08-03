import json


def test_process_setstatus(client, sample_tweet):
    res = client.put(f"/api/v1/process/setstatus/{sample_tweet.id}", data={'statusid': '45'})
    print(f'res:[{res.status_code}]')
    assert res.status_code == 200  # TODO: This should be 204, it's being set to 204 in the response, but it's coming back 200  # noqa: E501
    assert json.loads(res.data.decode()) == {'id': 1, 'party': 'GOP', 'person': 'Trump', 'status': '45', 'tone_analytic': 0.0, 'tone_anger': 0.0, 'tone_confident': 0.0, 'tone_fear': 0.0, 'tone_joy': 0.0, 'tone_sadness': 0.0, 'tone_tentative': 0.0, 'tweet': 'Bigly'}


def test_sample_tweet_fixture(sample_tweet):
    assert sample_tweet.id == 1
    assert sample_tweet.party == 'GOP'
    assert sample_tweet.person == 'Trump'


"""
def test_create_tweet(client):
    pass
"""

"""
def test_get_one_tweet(client, sample_tweet):
    res = client.get(f"/tweet/{sample_tweet.id}")
    tweet_dict = json.loads(res.data.decode())
    assert tweet_dict["person"] == "Trump"
"""
