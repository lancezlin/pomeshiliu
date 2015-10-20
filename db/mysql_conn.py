'''
from mysql.connector import connection

cnx = connection.MySQLConnection(user='root', password='Pi=3.1415926', host='127.0.0.1', database='pomeshiliu')
cnx.close()
'''
import MySQLdb
try:
    cnx = MySQLdb.connect(host='localhost', user='root', passwd='Pi=3.1415926', db='pomeshiliu')
    print 'yes'
    cursor = cnx.cursor()
    
    cursor.execute("""SELECT cat_id FROM category""")
    data = cursor.fetchall()
    idlist = []
    for item in data:
        idlist.append(int(item[0]))
    print idlist

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