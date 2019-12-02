import pymysql
import conf
conn = pymysql.connect(host=conf.host,user=conf.user,password=conf.password,database=conf.database,charset=conf.charset)
cursor = conn.cursor()

gettbsql='show tables like \'%error_info\''
def execute(sql,conn,cursor):
	try:
        	cursor.execute(sql)
	except Exception as e:
        	conn.rollback()
        	print 'error rollback', e
        	exit(1)
    	else:
        	conn.commit()
        	print 'commit ok', cursor.rowcount
	return cursor.fetchall()
if __name__ == '__main__':
	tables=execute(gettbsql,conn,cursor)
	for table in tables:
		clearsql1='delete from '+table[0]+' where datetime < date_add(now(), interval -1 month);'
		clearsql2='delete from '+table[0]+' where errortype like \'%read ECONNRESET%\''
		clearsql3="delete from "+table[0]+" where errortype like '%Error: ETIMEDOUT%';"
		clearsql4='delete from '+table[0]+' where errortype=\'Incorrect format did not get a specific type\''
		execute(clearsql1,conn,cursor)
		execute(clearsql2,conn,cursor)
		execute(clearsql3,conn,cursor)
		execute(clearsql4,conn,cursor)
        cursor.close()
        conn.close()
