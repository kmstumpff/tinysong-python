
import urllib2
import json

API_KEY = ''  # fill in with your key
API_URL = 'http://tinysong.com/'
API_FORMAT = 'json'
global TS_ONE_RESULT
TS_ONE_RESULT = "a/"
global TS_ONE_WITH_METADATA
TS_ONE_WITH_METADATA = "b/"
global TS_MULTIPLE_WITH_METADATA
TS_MULTIPLE_WITH_METADATA = "s/"
global TS_CHOICE
TS_CHOICE = ""


class Query:
    def __init__(self):
        self.json = []
        self.length = 0

    def check_results(self):
        if self.json:
            return True
        else:
            return False

    def get_title(self, numb):
        return self.json[numb]['SongName']

    def get_songid(self, numb):
        return self.json[numb]['SongID']


    def get_artist(self, numb):
        return self.json[numb]['ArtistName']


    def get_album(self, numb):
        return self.json[numb]['AlbumName']


    def get_albumid(self, numb):
        return self.json[numb]['AlbumID']


    def get_url(self, numb):
        return self.json[numb]['Url']


    def api_call(self, query, ret_type, limit=5):
        if ret_type == 1:
            TS_CHOICE = TS_ONE_RESULT
        if ret_type == 2:
            TS_CHOICE = TS_ONE_WITH_METADATA
        if ret_type == 3:
            TS_CHOICE = TS_MULTIPLE_WITH_METADATA
            C_LIMIT="&limit=" + str(limit)
        else:
            TS_CHOICE = TS_MULTIPLE_WITH_METADATA
            C_LIMIT=""
        req = API_URL+TS_CHOICE+query.replace(" ", "+")+"?format="+API_FORMAT+"&key="+API_KEY+C_LIMIT
        # print("request: " + req)
        response = urllib2.urlopen(req.lower()).read()
        self.json = json.loads(response)
        self.length = len(self.json)
    

class APIError(Exception):
    
    def __init__(self, value):
        self.message = value

    def __str__(self):
        return repr("There was a problem with your API request: " + self.message)
        
        

