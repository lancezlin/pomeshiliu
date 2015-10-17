import json
import urllib
import urllib2

tax_api_url = 'http://api.walmartlabs.com/v1/taxonomy?apiKey=f2v2kpfp5jnrk5mzp9unjjb3'

while True:
    req = urllib2.Request(tax_api_url)
    url_open = urllib2.urlopen(req)
    data = url_open.read()
    try:
        js = json.loads(data)
    except:
        js = None
        print 'No data retrieved!!'

    print json.dumps(js, indent=4)

    for i in xrange(5):
        catId = js["categories"][i]["id"]
        catName = js["categories"][i]["name"]
        print catId
        print catName

    break

