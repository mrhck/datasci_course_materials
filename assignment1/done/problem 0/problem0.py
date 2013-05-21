import json
import urllib

request = "http://search.twitter.com/search.json?q=microsoft&page="
for i in range(10):
    page = i + 1
    response = urllib.urlopen(request + str(page))
    print json.load(response)
