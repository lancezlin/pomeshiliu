import json
import urllib
import urllib2
import MySQLdb
#import mysql.connector
#from mysql.connector import errorcode


tax_api_url = 'http://api.walmartlabs.com/v1/taxonomy?apiKey=f2v2kpfp5jnrk5mzp9unjjb3'

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

    print json.dumps(js, indent=4)

    for cat in js['categories']:
        catId = cat['id']
        catName = cat['name']
        catPath = cat['path']
        
        for subcat in cat['children']:
            subCatId = subcat['id']
            subCatName = subcat['name']
            subCatPath = subcat['path']
            try:
                for subsubcat in subcat['children']:
                    subSubCatId = subsubcat['id']
                    subSubCatName = subsubcat['name']
                    subSubCatPath = subsubcat['path']
                    print catId, catName, catPath, subCatPath, subSubCatPath    
            except:
                pass
    break
    
try:
    cnx = MySQLdb.connect(host='localhost', user='root', passwd='Pi=3.1415926', db='pomeshiliu')
    print 'yes'
    cursor = cnx.cursor()
    
    cursor.execute("""SELECT * FROM category""")
    data = cursor.fetchall()
    print data

    '''
    cursor.execute("""INSERT INTO category (cat_id, cat_name, cat_path, company_name) VALUES (%s, %s, %s, %s)""", (1, "Toys", "Toys", "Walmart"))
    data = cursor.fetchall()
    if len(data) is 0:
        cnx.commit()
        '''
    cursor.close()



    cnx.close()
except:
    print "cannot connect to mysql"