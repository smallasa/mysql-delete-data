#!/usr/bin/env python
#coding:utf-8

'''
@author: smallasa
@email : smallasa@sina.com
'''

from lib import db_conn
import time
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='sql_operation_error.log',
                filemode='w')

db_name=sys.argv[1]
table_name=sys.argv[2]
column_name=sys.argv[3]
start_optime=int(sys.argv[4])
end_optime=int(sys.argv[5])

db_name=db_name.strip()
table_name=table_name.strip()
column_name=column_name.strip()

db_user='<username>'
db_pass='<password>'
db_host='<ip_addr>'
db_port=<port>

if db_name and table_name and column_name and start_optime and end_optime:
    if start_optime > end_optime:
        sys.exit(1)
    else:
        recursion_optime=start_optime+60000
        while True:
            conn=db_conn.Db_conn(db_user,db_pass,db_port,db_host,db_name)
            if recursion_optime>end_optime:
                recursion_optime=end_optime
            sql='delete from %s where %s>=%d and %s<%d' % (table_name,column_name,start_optime,column_name,recursion_optime)
            op_result=conn.mysql_op(sql,'write')
	    if op_result=='error':
                print '%s exec is \033[1;31m ERROR \033[0m,%s' % (db_name,sql)
		logging.error('database is %s,%s' % (db_name,sql))
            else:
                print '%d,%s exec is \033[1;36m OK \033[0m,%s' % (op_result,db_name,sql)
            if recursion_optime==end_optime:
                break
            else:
                start_optime=recursion_optime
                recursion_optime=start_optime+60000
else:
    print 'input args ERROR!'
    sys.exit(1)
