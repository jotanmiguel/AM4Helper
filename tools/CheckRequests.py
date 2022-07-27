import requests, json

def Check(request: requests.Response):
    codes = {
        '200' : 'OK',
        '400' : 'BAD REQUEST',
        '404' : 'NOT FOUND'
    }
    
    return codes[request.status_code]