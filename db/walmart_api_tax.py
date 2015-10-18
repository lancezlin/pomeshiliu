import json
import urllib
import urllib2

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
                '''try:
                    for subsubsubcat in subsubcat['children']:
                        subSubSubCatId = subsubsubcat['id']
                        subSubSubCatName = subsubsubcat['name']
                        subSubSubCatPath = subsubsubcat['path']
                        print catId, catName, catPath, subCatPath, subSubCatPath, subSubSubCatPath    
                except:
                    pass'''
    break

