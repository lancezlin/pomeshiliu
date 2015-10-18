from mysql.connector import connection

cnx = connection.MySQLConnection(user='root', password='Pi=3.1415926', host='127.0.0.1', database='pomeshiliu')
cnx.close()