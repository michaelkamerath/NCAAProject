import pymysql
import pymysql.cursors

conn = pymysql.connect(host="localhost",
                       user="root",
                       passwd="password",
                       db="ncaa",
                       charset="utf8",
                       cursorclass=pymysql.cursors.DictCursor)


cur = conn.cursor()
