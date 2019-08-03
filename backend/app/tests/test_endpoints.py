import json


def test_process_setstatus(client, sample_tweet):
    res = client.put(f"/api/v1/process/setstatus/{sample_tweet.id}", data={'statusid': '45'})
    print(f'res:[{res.status_code}]')
    assert res.status_code == 200  # TODO: This should be 204, it's being set to 204 in the response, but it's coming back 200  # noqa: E501
    data = json.loads(res.data.decode())
    assert data['status'] == '45'


def test_sample_tweet_fixture(sample_tweet):
    assert sample_tweet.id == 1
    assert sample_tweet.party == 'GOP'
    assert sample_tweet.person == 'Trump'


def test_create_tweet(client):
    tweet_info = {'party': 'GOP', 'person': 'Trump', 'tweet': 'Bigly'}
    res = client.post(f'/api/v1/tweet/create', data=tweet_info)
    assert res.status_code == 200

    data = json.loads(res.data.decode())
    assert data['party'] == 'GOP'
    assert data['person'] == 'Trump'
    assert data['tweet'] == 'Bigly'


def test_get_one_tweet(client, sample_tweet):
    print(f'tweet:[{sample_tweet.to_dict()}]')
    res = client.get(f'/api/v1/tweet/{sample_tweet.id}')
    print(f'res.data:[{res.data}]')
    tweet_dict = json.loads(res.data.decode())
    assert tweet_dict["person"] == "Trump"
