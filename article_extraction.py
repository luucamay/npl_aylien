from aylienapiclient import textapi
import api_access

client = textapi.Client(api_access.id, api_access.key)

url = "http://techcrunch.com/2015/04/06/john-oliver-just-changed-the-surveillance-reform-debate"
extract = client.Extract({"url": url, "best_image": True})

print(type(extract))
print(extract["title"])
