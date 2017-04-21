#!/usr/bin/python
# coding:utf8
import MySQLdb
import sys
reload(sys)

class Db_conn():
    def __init__(self,db_user,db_pass,db_port,db_host,db_name):
        self.db_type='mysql'
        self.db_user=db_user
        self.db_pass=db_pass
        self.db_port=db_port
        self.db_name=db_name
        self.db_host=db_host

    def mysql_op(self,sql,op_type='read',Result_Status='Dict'):
        if op_type=='read':
            try:
                dblink = MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=self.db_port,db=self.db_name,connect_timeout=5,charset='utf8')
            except Exception as e:
                print e
            if Result_Status == 'Tuple':   #返回元组作为结果集
                cursor = dblink.cursor()
            elif Result_Status=='Dict':    #返回字典作为结果集
                cursor = dblink.cursor(MySQLdb.cursors.DictCursor)
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
            except Exception as e:
                print e
                return 0
            cursor.close()
            dblink.close()
            return result
        if op_type=='write':
            try:
                dblink = MySQLdb.connect(host=self.db_host,user=self.db_user,passwd=self.db_pass,port=self.db_port,db=self.db_name,connect_timeout=5,charset='utf8')
            except Exception as e:
                print e
            try:
                cursor = dblink.cursor()
                n=cursor.execute(sql)
            except Exception as e:
                print e
                return 'error'
            dblink.commit()
            cursor.close()
            dblink.close()
            return n
