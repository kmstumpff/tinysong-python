#import hashlib 
#import hmac
import urllib2
import simplejson

API_KEY = '' #fill in with your key
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

def get_title(ret, numb):
    return ret[numb]['SongName']

def get_songid(ret, numb):
    return ret[numb]['SongID']

def get_artist(ret, numb):
    return ret[numb]['ArtistName']

def get_album(ret, numb):
    return ret[numb]['AlbumName']

def get_albumid(ret, numb):
    return ret[numb]['AlbumID']

def get_url(ret, numb):
    return ret[numb]['Url']

def api_call(query, ret_type, limit=5, parameters={}):
    if ret_type == 1:
        TS_CHOICE = TS_ONE_RESULT
    if ret_type == 2:
        TS_CHOICE = TS_ONE_WITH_METADATA
    if ret_type == 3:
        TS_CHOICE = TS_MULTIPLE_WITH_METADATA
        C_LIMIT="&limit=" + str(limit)
    else:
        C_LIMIT=""
    req = API_URL+TS_CHOICE+query.replace (" ", "+")+"?format="+API_FORMAT+"&key="+API_KEY+C_LIMIT
    print("request: " + req)
    response = urllib2.urlopen(req.lower()).read()
    return simplejson.loads(response)
    

class APIError(Exception):
    
    def __init__(self, value):
        self.message = value
    def __str__(self):
        return repr("There was a problem with your API request: " + self.message)
        
        

