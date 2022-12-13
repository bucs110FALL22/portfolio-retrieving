import requests

class IPAPI:
    '''
    gets data about your ip address and your latitude, longitutde, and more
    '''

    def __init__(self):
        '''
        initializes variables and returns the api link
        '''
        self.url = 'https://api.techniknews.net/ipgeo/'

    def getcountry(self):
        '''
        defines your latitude returns none
        '''
        r = requests.get(self.url)
        response = r.json()
        if response.get('lat'):
            return response['lat']
        else:
            return None
   