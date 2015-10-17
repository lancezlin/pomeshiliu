import json
import urllib
import urllib2

tax_api_url = 'http://api.walmartlabs.com/v1/taxonomy?apiKey=f2v2kpfp5jnrk5mzp9unjjb3'

while True:
	url_open = urllib.url_open(tax_api_url)
	data = url_open.read()
	try:
		js = json.loads(data)
	except:
		js = None
		print 'No data retrieved!!'

	