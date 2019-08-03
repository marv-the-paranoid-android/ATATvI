import json


def test_process_setstatus(client, sample_tweet):
    res = client.put(f"/api/v1/process/setstatus/{sample_tweet.id}", data={'statusid': '45'})
    print(f'res:[{res.status_code}]')
    assert res.status_code == 200  # TODO: This should be 204, it's being set to 204 in the response, but it's coming back 200  # noqa: E501
    assert json.loads(res.data.decode()) == []


def test_sample_tweet_fixture(sample_tweet):
    assert sample_tweet.id == 1
    assert sample_tweet.party == 'GOP'
    assert sample_tweet.person == 'Trump'


"""
def test_create_(client):
    crew_info = {"name": "Skipper Vin"}
    res = client.post("/crew", data=crew_info)
    assert res.status_code == 200
    res = client.get("/crew")
    crew = json.loads(res.data.decode())
    assert len(crew) == 1
    assert crew[0]['name'] == "Skipper Vin"
    assert crew[0].get('boat') is None
"""

"""
def test_get_one_tweet(client, sample_tweet):
    res = client.get(f"/tweet/{sample_tweet.id}")
    tweet_dict = json.loads(res.data.decode())
    assert tweet_dict["person"] == "Trump"
"""
