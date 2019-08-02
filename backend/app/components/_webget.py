import requests
import abc
import json
from os import environ
from flask import jsonify, Response


class WebGet:
    __metaclass__ = abc.ABCMeta

    mock_filename = '';

    def __init__(self, mock_filename: str=''):
        self.mock_filename = mock_filename

    def serialize(self):
        return vars(self)

    @staticmethod
    def getRawData(url : str, headers : dict, selector: str) -> (bool, requests.models.Response, str, str):
        # Perform: Get against URL
        validGet = False
        errmsg = ''
        rawdata = ''
        response = requests.get(url, headers = headers)
        #print(f'!! DEBUG !!: getRaw()::response:[{response}]')
        #print(f'!! DEBUG !!: getRaw()::response.text:[{response.text}]')

        # Error Handling and Data-Validation
        if isinstance(response, requests.models.Response):
            if response.status_code == 200:
                rawdata = response.json()
                if selector in rawdata:
                    results = rawdata.get(selector, '')
                    if type(results) == 'list' or len(results) > 0:
                        rawdata = results
                        validGet = True

        if not validGet:
            errmsg = json.dumps({'invalidGet': json.dumps(response.json())})

        return validGet, rawdata, response, errmsg

    def getMock(self) -> requests.models.Response:
        with open('./mocks/'+self.mock_filename, 'r') as jsonfile:
           data = json.load(jsonfile)
        return(Response(
            json.dumps(data),
            status=200,
            content_type='application/json'
        ))

    @abc.abstractmethod
    def _makeURL(self, query, lat, long : str) -> (str, dict):
        pass

    def getData(self, query, lat, long, selector : str) -> str:
        if query is None or query == '':
            return json.dumps({"error": "ERROR: Query==None"})

        # Craft URL
        url, headers = self._makeURL(query, lat, long)

        # Get Data
        validGet, data, response, errmsg = self.getRawData(url, headers, selector)
        if not validGet: # RESEARCH: Change to use v3.8 Walrus operator?!?
            return errmsg

        return json.dumps(data)
