import requests

picture = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=false%22).json()

print(picture)