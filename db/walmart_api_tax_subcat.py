import json
import urllib
import urllib2
import MySQLdb

tax_api_url = 'http://api.walmartlabs.com/v1/taxonomy?apiKey=f2v2kpfp5jnrk5mzp9unjjb3'


try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='Pi=3.1415926', db='pomeshiliu')
    cursor = conn.cursor()

    while True:
        req = urllib2.Request(tax_api_url)
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

        json.dumps(js, indent=4)
        # sub category collecting:
        for cat in js['categories']:
            catId = cat['id']
            catName = cat['name']
            catPath = cat['path']
            for subcat in cat['children']:
                subCatId = subcat['id']
                subCatName = subcat['name']
                subCatPath = subcat['path']
                cursor.execute("""INSERT INTO subcategory (subcat_id, subcat_name, subcat_path, parent_cat) VALUES (%s, %s, %s, %s)""", (subCatId, subCatName, subCatPath, catId))
                response = cursor.fetchall()
                conn.commit()
        break
    cursor.close()
    conn.close()
except:
    print "error2"