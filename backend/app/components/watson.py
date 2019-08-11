import json
from os import environ
from app.components._webget import WebGet
from flask import Response
from requests.utils import quote


# @TODO make another class to encapsulate the data processing (from routes.py)
# and use composition to merge it into the Watson class

class Watson(WebGet):

    text = ''

    def __init__(self, text, mock_filename: str):
        self.text = text
        super().__init__(mock_filename)
        self.setUserPasswd('apikey', environ.get('IBM_WATSON_TONALITY_APIKEY'))

    def _makeURL(self) -> (str, dict):
        return environ.get('IBM_WATSON_TONALITY_URL') + '/v3/tone?version=2017-09-21&sentences=false&text=' + quote(self.text), {}  # noqa: E221 E501

    def getData(self, selector: str) -> str:
        data = json.loads(super().getData(selector))

        # Grab just the data we want to the return
        print(f'data:[{data}]')

        return (Response(
            json.dumps(data),
            status=200,
            content_type='application/json'
        ))
