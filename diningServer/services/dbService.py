import pymysql

conn = pymysql.connect(host="34.64.201.21",
                       user="root",
                       password="0000",
                       db="diningdb",
                       charset="utf8")

cur = conn.cursor()

insert = "insert into test_table(t_id, t_pw, t_name) values('t', 'bbbb', 'pypy');"

cur.execute(insert)
conn.commit()

sql = "SELECT * from dining_table"
cur.execute(sql)
result = cur.fetchall()

print(result)



def request(data):
    print("test signup", data)
    return data


