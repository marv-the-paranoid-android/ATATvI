import requests
import abc
import json
from flask import Response


class WebGet:
    __metaclass__ = abc.ABCMeta

    mock_filename = ''
    user = ''
    passwd = ''

    def __init__(self, mock_filename: str = ''):
        self.mock_filename = mock_filename

    def setUserPasswd(self, user, passwd):
        self.user = user
        self.passwd = passwd

    def serialize(self):
        return vars(self)

    @staticmethod
    def validateData(rawdata, selector: str) -> bool:
        if selector == '':
            return True

        if selector in rawdata:
            results = rawdata.get(selector, '')
            if type(results) == 'list' or len(results) > 0:
                rawdata = results
                return True

        return False

    @staticmethod
    def getRawData(url: str, headers: dict, selector: str, user: str = '', passwd: str = '') -> (bool, requests.models.Response, str, str):  # noqa:501
        # Perform: Get against URL
        validGet = False
        errmsg = ''
        rawdata = ''
        if user == '':
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url, headers=headers, auth=(user, passwd))

        # Error Handling and Data-Validation
        if isinstance(response, requests.models.Response):
            if response.status_code == 200:
                rawdata = response.json()
                validGet = WebGet.validateData(rawdata, selector)

        if not validGet:
            errmsg = json.dumps({'invalidGet': json.dumps(response.json())})

        return validGet, rawdata, response, errmsg

    def getMock(self, selector: str) -> requests.models.Response:
        with open('./mocks/' + self.mock_filename, 'r') as jsonfile:
            rawdata = json.load(jsonfile)
        validGet = WebGet.validateData(rawdata, selector)
        if validGet:
            return(Response(
                json.dumps(rawdata),
                status=200,
                content_type='application/json'
            ))
        else:
            print(f'Selector:[{selector}] not found in rawdata')

    @abc.abstractmethod
    def _makeURL(self) -> (str, dict):
        pass

    def getData(self, selector: str) -> str:

        # Craft URL
        url, headers = self._makeURL()

        # Get Data
        validGet, data, response, errmsg = self.getRawData(url, headers, selector, self.user, self.passwd)  # noqa:501
        if not validGet:  # RESEARCH: Change to use v3.8 Walrus operator?!?
            return errmsg

        return json.dumps(data)
