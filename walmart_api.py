import json
import urllib
import urllib2

walmarturl = 'http://api.walmartlabs.com/v1/search?apiKey=f2v2kpfp5jnrk5mzp9unjjb3&'

while True:
	product = raw_input('search product:')
	if len(product) < 1:
		break

	values = urllib.urlencode({'query' : product})
	req_url = urllib2.Request(walmarturl + values)
	print 'retrieving', req_url

	url_open = urllib2.urlopen(req_url)
	data = url_open.read()
	print len(data), "characters."

	try:
		js = json.loads(data)
	except:
		js = None
		print 'json null'

#	if 'status' not in js or js['status'] != 'OK':
#		print '====== Failure to retrieve ======'
#		print data
#		continue
	
	print json.dumps(js, indent = 4)
	item_id = js['items'][0]['itemId']
	prod_name = js['items'][0]['name']

	print "first item id is: ", item_id
	print "first item name is: ", prod_name
	break
'''
try:
	import urllib
	print "urllib installed"
except ImportError:
	print "Error"
	'''