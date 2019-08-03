import json


def test_process_setstatus(client, sample_tweet):
    res = client.put(f"/api/v1/process/setstatus/{sample_tweet.id}", data={"statusid": "45"})
    assert res.status_code == 204
    assert json.loads(res.data.decode()) == []


"""
def test_sample_crew_fixture(sample_crew):
    assert sample_crew.id == 1
    assert sample_crew.name == "Quinn"


def test_solo_crew_fixture(solo_crew):
    assert solo_crew.id == 1
    assert solo_crew.name == "Skipper Vin"


def test_create_crew_with_boat(client, sample_boat):
    crew_info = {"name": "Quinn", "boat": sample_boat.id}
    res = client.post("/crew", data=crew_info)
    assert res.status_code == 200

def test_create_(client):
    crew_info = {"name": "Skipper Vin"}
    res = client.post("/crew", data=crew_info)
    assert res.status_code == 200
    res = client.get("/crew")
    crew = json.loads(res.data.decode())
    assert len(crew) == 1
    assert crew[0]['name'] == "Skipper Vin"
    assert crew[0].get('boat') is None


def test_get_one_crew(client, sample_crew):
    res = client.get(f"/crew/{sample_crew.id}")
    crew_dict = json.loads(res.data.decode())
    assert crew_dict["name"] == "Quinn"
"""
