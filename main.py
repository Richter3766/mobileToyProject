import pymysql

conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="0000",
                       db="testdb",
                       charset="utf8")

cur = conn.cursor()

# insert = "insert into test_table(t_id, t_pw, t_name) values('t', 'bbbb', 'pypy');"
#
# cur.execute(insert)
# conn.commit()

sql = "SELECT * from test_table"
cur.execute(sql)
result = cur.fetchall()

print(result)

