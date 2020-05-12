#!usr/bin/env python
import configobj
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
