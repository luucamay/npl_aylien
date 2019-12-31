import urllib.request, json
# with urllib.request.urlopen("https://techcrunch.com/2019/12/22/who-will-the-winners-be-in-the-future-of-fintech/") as url:
with urllib.request.urlopen("https://fcc-weather-api.glitch.me/api/current?lat=35&lon=139") as url:
    data = json.loads(url.read().decode())
    print (data)

