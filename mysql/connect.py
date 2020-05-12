#!usr/bin/env python

import pymysql as mysql
import configobj

'''
author:Yel
date:2020-5-12
Mysql连接类
'''

class Connect:
	connect = '';
	error = '';
	success = '';
	_host = '';
	_port = '';
	_table = '';
	_user = '';
	_password = '';
	# 初始连接
	def __init__(self,db_host = '',db_port = '',db_table = '',db_user = '',db_pwd = ''):
		self._host = db_host;
		self._port = int(db_port);
		self._table = db_table;
		self._user = db_user;
		self._password = db_pwd;
		
	

	#连接
	def run(self):
		connect = mysql.connect(host=self._host,port=self._port,db=self._table,user=self._user,password=self._password,charset='utf8');
		con = connect.cursor()
		print(con.query('SELECT * FROM order'))
		self.connect = connect;


	def getConnect(self):
		return self.connect;

	# 错误信息
	def error(self):
		pass
	# 连接成功信息
	def success(self):
		pass



# 读取配置文件
class Config:

	file = '';

	def __init__(self,file = ''):
		if file != '':
			self.file = file;
		else:
			self.file = 'config.ini';

	# 获取配置
	def getConfig(self):
		return configobj.ConfigObj(self.file,encoding="UTF8");


