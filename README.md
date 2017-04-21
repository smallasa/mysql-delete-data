# mysql-delete-data
*mysql 清理数据脚本(delete 删除数据)*

1. 脚本说明
```text
此脚本只作为参考,请根据实际情况进行修改!
```

2. 编辑文件clear_data.py
```text
db_user='<username>'
db_pass='<password>'
db_host='<ip_addr>'
db_port=<port>
```

3. 安装python库
```bash
pip install MySQL-python
```

4. 执行
```bash
python clear_data.py <dbname> <table> <fieldname> <begintime> <endtime>
```
