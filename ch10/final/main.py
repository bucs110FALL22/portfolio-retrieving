from fish import Fish
from ip import IPAPI
def main(): 
  '''
  running and returns both classes
  '''
  country = IPAPI().getcountry()
  fish = Fish(country) 
  fishname = fish.getfishlat()
  print(fishname)
main()