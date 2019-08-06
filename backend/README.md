# Back End

This is the backend for the ATATvI project, written in Python and using Flask, serveral
end-points are published for consuming data and triggering work to be processed.

## How to  Install

Invoke PipEnv Shell:
`pipenv shell`

Install Dependencies:
`pipenv install`

On DB Changes:

```bash
rm app.db
rm -rf migrations
flask db init
flask db migrate
flask db upgrade
```

## How to Run

`flask run`

## API

### Prequests for IBM Watson Tone Analyzer

.env should have the following information with your credentials...

```bash
IBM_WATSON_TONALITY_APIKEY = djksjdfj$9uRI#JDdj39d#JD#JD#Db2t_M-5tH3QpGPK
IBM_WATSON_TONALITY_URL    = https://gateway.watsonplatform.net/tone-analyzer/api
```

### Tweek

This family of functions is dedicated to individual actions regarding
a tweet record.

#### GET Tweet

GET with a tweet `id` will return the Tweet() object via ORM

##### Example: GET Tweet

```bash
http GET :5000/api/v1/tweet/1
```

```http
HTTP/1.0 200 OK
Content-Length: 198
Content-Type: application/json
Date: Sun, 04 Aug 2019 03:27:29 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

{
    "id": 1,
    "party": "gop",
    "person": "trump",
    "status": "0",
    "tone_analytic": 0.0,
    "tone_anger": 0.0,
    "tone_confident": 0.0,
    "tone_fear": 0.0,
    "tone_joy": 0.0,
    "tone_sadness": 0.0,
    "tone_tentative": 0.0,
    "tweet": "bigly"
}
```

#### GET Tweets (All)

GET all Tweets as an array of Tweet() objects from ORM

#### Example: GET Tweets (All)

```bash
http GET :5000/api/v1/tweets
```

```http
HTTP/1.0 200 OK
Content-Length: 411
Content-Type: application/json
Date: Sun, 04 Aug 2019 04:09:26 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

[
    {
        "id": 1,
        "party": "gop",
        "person": "trump",
        "status": "0",
        "tone_analytic": 0.0,
        "tone_anger": 0.0,
        "tone_confident": 0.0,
        "tone_fear": 0.0,
        "tone_joy": 0.0,
        "tone_sadness": 0.0,
        "tone_tentative": 0.0,
        "tweet": "bigly"
    },
    {
        "id": 2,
        "party": "gop",
        "person": "trump",
        "status": "0",
        "tone_analytic": 0.0,
        "tone_anger": 0.0,
        "tone_confident": 0.0,
        "tone_fear": 0.0,
        "tone_joy": 0.0,
        "tone_sadness": 0.0,
        "tone_tentative": 0.0,
        "tweet": "MexicoWillPayForIt"
    }
]
```

#### POST Tweet (Create)

POST with a Tweet() object via the ORM, will create a tweet record

##### Example: POST Tweet (Create)

```bash
http POST :5000/api/v1/tweet/create party=gop person=trump tweet=bigly
```

```http
HTTP/1.0 200 OK
Content-Length: 198
Content-Type: application/json
Date: Sun, 04 Aug 2019 03:25:52 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

{
    "id": 1,
    "party": "gop",
    "person": "trump",
    "status": "0",
    "tone_analytic": 0.0,
    "tone_anger": 0.0,
    "tone_confident": 0.0,
    "tone_fear": 0.0,
    "tone_joy": 0.0,
    "tone_sadness": 0.0,
    "tone_tentative": 0.0,
    "tweet": "bigly"
}
```

#### GET Tweet (Pending Analysis)

GET a Tweet() object via the ORM, that is needing to be analyzed (status=='0')

#### Example: GET Tweet (Pending Analysis)

`/api/v1/process/getpending`

```bash
http GET :5000/api/v1/process/getpending
```

```http
HTTP/1.0 200 OK
Content-Length: 456
Content-Type: application/json
Date: Fri, 02 Aug 2019 23:36:20 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

{
    "id": 1,
    "party": "GOP",
    "person": "Trump",
    "status": "0",
    "tone_analytic": null,
    "tone_anger": null,
    "tone_confident": null,
    "tone_fear": null,
    "tone_joy": null,
    "tone_sadness": null,
    "tone_tentative": null,
    "tweet": "Bigly"
}
```

#### PUT Tweet Status

Allows for the setting of a tweet's status (used for processing tweets sent to Watson
for analysis):

Status | Desc
-------|-----
0 | Queued and Ready
1 | In processed
2 | Complete
99 | Error

#### Example PUT Tweet Status

`/api/v1/process/setstatus/<int:id> (BODY == statusid='99')`

```bash
http PUT :5000/api/v1/process/setstatus/1 statusid=99
```

```http
HTTP/1.0 200 OK
Content-Length: 457
Content-Type: application/json
Date: Sat, 03 Aug 2019 00:07:25 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

{
    "id": 1,
    "party": "GOP",
    "person": "Trump",
    "status": "99",
    "tone_analytic": null,
    "tone_anger": null,
    "tone_confident": null,
    "tone_fear": null,
    "tone_joy": null,
    "tone_sadness": null,
    "tone_tentative": null,
    "tweet": "Bigly"
```

### Do Work

When triggered with a tweet `id`, a request will be made to IBM Watson
Tone Analyzer. During this process, the `getwork()` is called to obtain
a record, `setstatus()` is called to change the status to `1==In Process`,
the data is sent to Watson and the reply is interrogated. If successful,
the status is changed to `2==Complete` and the tweet will be available
in the next `report()` call.

### Example: Do Work

`/api/v1/process/dowork/<int:id>`

```bash
http PUT :5000/api/v1/process/dowork/1
```

```http
HTTP/1.0 200 OK
Content-Length: 212
Content-Type: application/json
Date: Tue, 06 Aug 2019 16:49:40 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

{
    "id": 1,
    "party": "GOP",
    "person": "Trump",
    "status": "2",
    "tone_analytic": null,
    "tone_anger": null,
    "tone_confident": null,
    "tone_fear": null,
    "tone_joy": null,
    "tone_sadness": 0.766478,
    "tone_tentative": null,
    "tweet": "Tweet"
}
```

### Report

Averaged score, for each category, aggregated and group by political party. Score is based 0.0 to 1.0, however only >= 0.4 is included.

### Example: Report

`/api/v1/report`

```bash
http GET :5000/api/v1/report
```

```http
HTTP/1.0 200 OK
Content-Length: 244
Content-Type: application/json
Date: Sat, 03 Aug 2019 03:00:26 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

{
    "parties": [
        {
            "analytic": 0.1,
            "anger": 0.75,
            "confident": 0.51,
            "fear": 0.69,
            "joy": 0.0,
            "party": "GOP",
            "sadness": 0.88,
            "tentative": 0.22
        },
        {
            "analytic": 0.52,
            "anger": 0.1,
            "confident": 0.49,
            "fear": 0.11,
            "joy": 0.7,
            "party": "DEM",
            "sadness": 0.51,
            "tentative": 0.53
        }
    ]
}
```

### Analyze tweet functions

Offering the ability to interact with the chart, clicking on one of the seven sentiments that our app analyzes will bring you to a path extension which will display all tweets with a rating at or above 0.4 in the associated sentiments category. (i.e. all tweets made up of at least 40% analytical tones). 

