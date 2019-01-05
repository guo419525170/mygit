# -*- coding: UTF-8 -*-
import pymysql
out_put='C:\\Users\Administrator\Desktop\schema_sync\logs\dbsync20181211_215456.sql'
def sql_exexute(coursor,f):
    sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
    sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]
    try:
        for sql_item in sql_list:
            sql = sql_item + ";"
            print(sql)
            cursor.execute(sql)  # 将SQL放到同一事务中执行
            results = cursor.fetchall()
            print(results)
    except Exception as e:
        connect.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        connect.commit()  # 事务提交
        print('事务处理成功', cursor.rowcount)
    cursor.close()
if __name__ == '__main__':
    connect = pymysql.Connect(
        host='172.17.100.200',
        port=3306,
        user='root',
        passwd='JTCF@2017',
        db='test-yueyang',
        charset='utf8'
    )
    cursor = connect.cursor()
    with open(out_put, 'r+',encoding="utf-8") as f:
         #sql_exexute(cursor,f)
        print("aaaaaaaa")
    connect.close()