import json
import urllib
import urllib2
import MySQLdb
#import mysql.connector
#from mysql.connector import errorcode


feed_api_url = 'http://api.walmartlabs.com/v1/feeds/items?apiKey=f2v2kpfp5jnrk5mzp9unjjb3&'
try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='Pi=3.1415926', db='pomeshiliu')
    cursor = conn.cursor()

    while True:
        cursor.execute("""SELECT cat_id FROM category""")
        IDs = cursor.fetchall()
        #categoryIds = []
        for item in IDs:
        #    categoryIds.append(str(item[0]))
            values = urllib.urlencode({'categoryId' : int(item[0])})
            req = urllib2.Request(feed_api_url + values)
            try:
                url_open = urllib2.urlopen(req)
            except IOError, e:
                if hasattr(e, 'reason'):
                    print e.Reason
                elif hasattr(e, 'code'):
                    print e.code
            data = url_open.read()
            try:
                js = json.loads(data)
            except:
                js = None
                print 'No data retrieved!!'

            print json.dumps(js, indent=4)

        #if len(categoryIds) > 0:

        break
    #conn.commit()
    cursor.close()
    conn.close()
except:
    print "error1"
