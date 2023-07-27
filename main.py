from flask import Flask

from diningServer.routes import routes_list


def create_app():
    app = Flask(__name__)

    # routes list
    # from toy.routes import routes_list
    # routes_list(app)

    routes_list(app)

    return app


app1 = create_app()
app1.run('0.0.0.0', port=5000, debug=False)


# import pymysql
#
# conn = pymysql.connect(host="127.0.0.1",
#                        user="root",
#     1                   password="0000",
#                        db="testdb",
#                        charset="utf8")
#
# cur = conn.cursor()
#
# # insert = "insert into test_table(t_id, t_pw, t_name) values('t', 'bbbb', 'pypy');"
# #
# # cur.execute(insert)
# # conn.commit()
#
# sql = "SELECT * from test_table"
# cur.execute(sql)
# result = cur.fetchall()
#
# print(result)
#
