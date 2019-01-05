
#传入表名，获取所有的列
def clumn_get(cursor,tab,db):
    column_list=[]
    sql = "select column_name from information_schema.columns where table_name= '%s'and table_schema='%s'" %(tab,db)
    try:
        cursor.execute(sql)  # 执行sql语句
        results = cursor.fetchall()
        for column in range(len(results)):
            column_list.append(results[column][0])
    except Exception as e:
        raise e
    return  column_list

#获取修改字段的前一个字段名
def front_clumn_get(cursor,tab,db,ziduan):
    column_list=[]
    sql = "select column_name from information_schema.columns,(select ordinal_position - 1 as ordinal  from information_schema.columns where table_name= '%s'and table_schema='%s' AND column_name = '%s') t where ordinal_position = t.ordinal and table_name= '%s'and table_schema='%s'"  %(tab,db,ziduan,tab,db)
    try:
        cursor.execute(sql)  # 执行sql语句
        results = cursor.fetchall()
        for column in range(len(results)):
            column_list.append(results[column][0])
    except Exception as e:
        raise e
    return  column_list



#传入字段属性名，获取字段属性,注意这里返回的是一个包含字段类型，是否为空，及默认值的list
def clumntype_get(cursor,tab,column_name,db):
    column_list_tpye=[]
    sql = "select COLUMN_TYPE,IS_NULLABLE,COLUMN_DEFAULT,COLUMN_COMMENT from information_schema.columns where table_name= '%s' and column_name ='%s' and table_schema = '%s'"  % (tab,column_name,db)
    try:
        cursor.execute(sql)  # 执行sql语句
        results = cursor.fetchone()
        for column in results:
            column_list_tpye.append(column)
    except Exception as e:
        raise e
    return column_list_tpye



#传入一个字段，修改类型，生成SQL,传入表名，字段名，字段类型，列表，生成列的模式
def column_sql(tab,column_name,column_type,mode,front_column):
    col_tpye=column_type[0]
    col_isnull=column_type[1]
    col_defaul=column_type[2]
    col_comment=column_type[3]
    if mode == 'c':
        col_front = front_column[0]
        if (col_isnull == 'YES' and col_defaul==None):  # 如果允许为空且无任何默认值
            sql = "alter table " + str(tab) + " modify column " + str(column_name) + " " + str(col_tpye)+" default null COMMENT \'"+str(col_comment) + "\' AFTER " + str(col_front) + " ;"
        elif(col_isnull == 'YES' and col_defaul!=None):#允许为空且有默认值
            sql = "alter table " + str(tab) + " modify column " + str(column_name) + " " + str(col_tpye) + " default "+ str(col_defaul) +" COMMENT \'" + str(col_comment) + "\' AFTER " + str(col_front) + " ;"
        elif (col_isnull != 'YES' and col_defaul==None): #不允许为空且无默认值
            sql = "alter table " + str(tab) + " modify column " + str(column_name) + " " + str(col_tpye)+ " not null COMMENT \'" + str(col_comment) + "\' AFTER " + str(col_front) + " ;"
        elif(col_isnull != 'YES' and col_defaul==''):#特殊情况，不允许为空且默认值为空格
            sql="alter table " + str(tab) + " modify column " + str(column_name) + " " + str(col_tpye)+ " not null"+ " default '' COMMENT \'" + str(col_comment) + "\' AFTER " + str(col_front) + " ;"
        else:  # 如果不允许为空，且设置了默认值 col_defaul != 'None':
            sql = "alter table " + str(tab) + " modify column " + str(column_name)+ " " + str(col_tpye)+" not null default " + str(col_defaul) + " COMMENT \'" + str(col_comment) + "\' AFTER " + str(col_front) + " ;"
    elif mode == 'a':
        col_front = front_column[0]
        if (col_isnull =='YES' and col_defaul==None):#如果允许为空，且无默认值
            sql = "alter table " + str(tab) + " add  column " + str(column_name)+ " " + str(col_tpye)+" COMMENT \'"+str(col_comment) + "\' AFTER " + str(col_front) + " ;"
        elif (col_isnull=='YES' and col_defaul!=None): #如果允许为空,且有默认值
            sql="alter table " + str(tab) + " add  column " + str(column_name)+ " " + str(col_tpye)+" NULL default "+str(col_defaul) +"COMMENT \'" + str(col_comment)+ "\' AFTER " + str(col_front) + " ;"
        elif (col_isnull !='YES' and col_defaul==None): #如果不允许为空，且没有默认值
            sql = "alter table " + str(tab) + " add  column " + str(column_name)+ " " + str(col_tpye)+" not null COMMENT \'"+str(col_comment) + "\' AFTER " + str(col_front) + " ;"
        else:  #如果不允许为空，且设置了默认值
            sql = "alter table " + str(tab) + " add  column " + str(column_name) + " " + str(col_tpye)+" not null default  "+str(col_defaul) +" COMMENT \'" + str(col_comment) + "\' AFTER " + str(col_front) + " ;"
    elif mode == 'd':
        sql = "alter table " + str(tab) + " drop column " + str(column_name)+";"
    return sql
