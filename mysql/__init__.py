#!usr/bin/env python
import connect

# 获取配置
config = connect.Config('../config.ini').getConfig();
mysql_config = config['mysql'];

# 连接数据库
con = connect.Connect(mysql_config['db_host'],mysql_config['db_port'],mysql_config['db_table'],mysql_config['db_user'],mysql_config['db_pwd']);

con.run()

# con.cursor()con
# print(con.execute('SELECT * FROM users'))