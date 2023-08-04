import pymysql

conn = pymysql.connect(host="34.64.201.21",
                       user="root",
                       password="0000",
                       db="diningdb",
                       charset="utf8",
                       # aws ec2
                       ssl_cert="/home/ubuntu/gcp_key/client-cert.pem",
                       ssl_key="/home/ubuntu/gcp_key/client-key.pem",
                       ssl_ca="/home/ubuntu/gcp_key/server-ca.pem")
                       # local
                       # ssl_cert="C:/Users/KHS/Desktop/gcp_key/client-cert.pem",
                       # ssl_key="C:/Users/KHS/Desktop/gcp_key/client-key.pem",
                       # ssl_ca="C:/Users/KHS/Desktop/gcp_key/server-ca.pem")

cur = conn.cursor()


def request(page):
    item_per_page = 10
    start_idx = (page - 1) * item_per_page

    sql = f"SELECT * " \
          f"FROM dining_table " \
          f"WHERE seq > {start_idx} " \
          f"AND seq <= {start_idx + item_per_page}"

    cur.execute(sql)
    result = cur.fetchall()
    return result
