import urllib2
import json


class Query:
    def __init__(self):
        self.json = []
        self.length = 0
        self.api_key = ''  # fill in with your key
        self.api_url = 'http://tinysong.com/'
        self.api_format = 'json'
        self.ret_1 = "a/"  # return one result
        self.ret_2 = "b/"  # return one result with metadata
        self.ret_3 = "s/"  # return multiple results with metadata
        self.ret_choice = ""

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
        # Check API key
        if not self.api_key:
            raise APIError("Missing API key")
        if ret_type == 1:
            self.ret_choice = self.ret_1
        if ret_type == 2:
            self.ret_choice = self.ret_2
        if ret_type == 3:
            self.ret_choice = self.ret_3
            lmt = "&limit=" + str(limit)
        else:
            self.ret_choice = self.ret_3
            lmt = ""
        req = self.api_url + self.ret_choice + query.replace(" ", "+") + "?format=" + self.api_format + "&key=" + self.api_key + lmt
        # print("request: " + req)
        response = urllib2.urlopen(req.lower()).read()
        self.json = json.loads(response)
        self.length = len(self.json)


class APIError(Exception):
    def __init__(self, value):
        self.message = value

    def __str__(self):
        return repr("There was a problem with your API request: " + self.message)
