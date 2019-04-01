import pymysql

# class common_functions(object):
#
# # ---- 需要初始化 __init__ 来连接数据库，并产生 self.cur 供后面函数应用
#     def __init__(self):
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='jiangning;123',
    db='school'
)
cur = conn.cursor()
cur.execute("SELECT * FROM course")
row_1 = cur.fetchone()
print(row_1)
