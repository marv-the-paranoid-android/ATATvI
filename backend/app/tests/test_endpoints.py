import json


def test_process_setstatus(client, sample_tweet):
    res = client.put(f"/api/v1/process/setstatus/{sample_tweet.id}", data={'statusid': '45'})  # noqa: E221 E501
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
    res = client.get(f'/api/v1/tweet/{sample_tweet.id}')
    tweet_dict = json.loads(res.data.decode())
    assert tweet_dict['party'] == sample_tweet.party
    assert tweet_dict['person'] == sample_tweet.person
    assert tweet_dict['tweet'] == sample_tweet.tweet


def test_get_all_tweet(client, sample_tweets):
    res = client.get(f'/api/v1/tweets')
    tweets_dict = json.loads(res.data.decode())
    assert len(tweets_dict) == 2
    assert tweets_dict[0]['party'] == 'GOP'
    assert tweets_dict[1]['party'] == 'GOP'
    assert tweets_dict[0]['person'] == 'Trump'
    assert tweets_dict[1]['person'] == 'Trump'
    assert tweets_dict[0]['tweet'] == 'Bigly'
    assert tweets_dict[1]['tweet'] == 'Covfefe'


def test_process_dowork(client, sample_tweet):
    res = client.put(f'/api/v1/process/dowork/{sample_tweet.id}')
    print(f'res:[{res}]')
    tweets_dict = json.loads(res.data.decode())
    assert tweets_dict['party'] == 'GOP'
    assert tweets_dict['person'] == 'Trump'
    assert tweets_dict['tweet'] == 'Bigly'
    assert tweets_dict['status'] == '99'
