import requests
import math

class Fish():
  '''
  uses the api to search through fish and determines a fish via your latitude
  '''
  def __init__(self, latitude): 
    '''
    initializes variables and returns the link and math to determine latitude
    '''
    self.url = 'https://www.fishwatch.gov/api/species/'
    self.lat = math.floor(latitude)
  def getfishlat(self): 
          '''
          gives you a fish based on your latitude
          '''
          r = requests.get('https://www.fishwatch.gov/api/species/')
          response = r.json()
          return response [self.lat]['Species Name']
            
          
              
           
          
