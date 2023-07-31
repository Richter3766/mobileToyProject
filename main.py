# from flask import Flask
#
# from diningServer.routes import routes_list
#
#
# def create_app():
#     app = Flask(__name__)
#
#     # routes list
#     # from toy.routes import routes_list
#     # routes_list(app)
#
#     routes_list(app)
#
#     return app
#
#
# app1 = create_app()
# app1.run('0.0.0.0', port=5000, debug=False)
#
#
import pymysql

conn = pymysql.connect(host="34.64.201.21",
                       user="root",
                       password="0000",
                       db="diningdb",
                       charset="utf8",
                       ssl_cert="/home/ubuntu/gcp_key/client-cert.pem",
                       ssl_key="/home/ubuntu/gcp_key/client-key.pem",
                       ssl_ca="/home/ubuntu/gcp_key/server-ca.pem")

cur = conn.cursor()

# insert = "insert into test_table(t_id, t_pw, t_name) values('t', 'bbbb', 'pypy');"
#
# cur.execute(insert)
# conn.commit()

sql = "SELECT * from dining_table"
cur.execute(sql)
result = cur.fetchall()

print(result)