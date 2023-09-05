
import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'password',
    auth_plugin='mysql_native_password'

)

# prepare cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE holyco")

print("DONE!")
"""

import pymysql
  
    # To connect MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root', 
    password = "MySQLpassword@5dollar.net"
    )
  
cur = conn.cursor()
      
"""