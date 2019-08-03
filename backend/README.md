# Back End

Desc of Back End
This is the backend for the ATATvI project, written in Python and using Flask, serveral
end-points are published for consuming data and triggering work to be processed.

## How to  Install

Invoke PipEnv Shell:
`pipenv shell`

Install Dependencies:
`pipenv install`

On DB Changes:
```
rm app.db
rm -rf migrations
flask db init
flask db migrate
flask db upgrade
```

## How to Run

`flask run`

## API


### Get Work
`/api/v1/process/getwork`
```
http GET :5000/api/v1/process/getwork

HTTP/1.0 200 OK
Content-Length: 456
Content-Type: application/json
Date: Fri, 02 Aug 2019 23:36:20 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

{
    "id": 1,
    "party": "GOP",
    "person": "TRUMP",
    "status": "0",
    "tone_analytic": null,
    "tone_anger": null,
    "tone_confident": null,
    "tone_fear": null,
    "tone_joy": null,
    "tone_sadness": null,
    "tone_tentative": null,
    "tweet": "Our great Republican Congressman John Ratcliffe is being treated very unfairly by the LameStream Media. Rather than going through months of slander and libel, I explained to John how miserable it would be for him and his family to deal with these people..."
}
```

## Set Status
`/api/v1/process/setstatus/<int:id> (BODY == statusid='99')`
```
http PUT :5000/api/v1/process/setstatus/1 statusid=34


HTTP/1.0 200 OK
Content-Length: 457
Content-Type: application/json
Date: Sat, 03 Aug 2019 00:07:25 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

{
    "id": 1,
    "party": "GOP",
    "person": "TRUMP",
    "status": "34",
    "tone_analytic": null,
    "tone_anger": null,
    "tone_confident": null,
    "tone_fear": null,
    "tone_joy": null,
    "tone_sadness": null,
    "tone_tentative": null,
    "tweet": "Our great Republican Congressman John Ratcliffe is being treated very unfairly by the LameStream Media. Rather than going through months of slander and libel, I explained to John how miserable it would be for him and his family to deal with these people..."
```

### Do Work
`/api/v1/process/dowork/<int:id>`
```
http PUT :5000/api/v1/process/dowork/1

HTTP/1.0 200 OK
Content-Length: 5
Content-Type: application/json
Date: Fri, 02 Aug 2019 21:28:52 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

null
```

### Report
`/api/v1/report`
```
http GET :5000/api/v1/report

HTTP/1.0 200 OK
Content-Length: 5
Content-Type: application/json
Date: Fri, 02 Aug 2019 21:29:39 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

null
```
