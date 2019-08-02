# Back End

Desc of Back End
This is the backend for the ATATvI project, written in Python and using Flask, serveral
end-points are published for consuming data and triggering work to be processed.

## How to  Install

Invoke PipEnv Shell
`pipenv shell`

Install Dependencies
`pipenv install`

## How to Run

`flask run`

## API


### Get Work
`/api/v1/process/getwork`
```
http GET :5000/api/v1/process/getwork

HTTP/1.0 200 OK
Content-Length: 5
Content-Type: application/json
Date: Fri, 02 Aug 2019 21:27:57 GMT
Server: Werkzeug/0.15.5 Python/3.7.4

null
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
