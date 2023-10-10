import pymysql

def insertStatus(status):
    conn = pymysql.connect(host='localhost', user='pjh', password='1234', db='shopping_db')
    cur = conn.cursor()
    cur.execute("insert into record_led(status) values('{0})".format(status))
    conn.commit()
    conn.close()