import json
import urllib
import urllib2
import MySQLdb
#import mysql.connector
#from mysql.connector import errorcode


feed_api_url = 'http://api.walmartlabs.com/v1/feeds/items?apiKey=f2v2kpfp5jnrk5mzp9unjjb3&categoryId=3944'

while True:
    #values = urllib.urlencode({'categoryId' : 2636})
    req = urllib2.Request(feed_api_url)
    try:
        url_open = urllib2.urlopen(req)
    except IOError, e:
        if hasattr(e, 'reason'):
            print e.reason
        elif hasattr(e, 'code'):
            print e.code
    data = url_open.read()
    try:
        js = json.loads(data)
    except:
        js = None
        print 'No data retrieved!!'
    print json.dumps(js, indent=4)
    break
