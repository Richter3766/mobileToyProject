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


def request():
    query = '''
            SELECT CONCAT('{', GROUP_CONCAT('"seq":', seq,
                                            ',"name":"', name,
                                            '","field":"', field,
                                            '","address":"', address, '"'), '}')
            FROM dining_table
            '''
    cur.execute(query)
    result = cur.fetchall()
    return result
