# Python_study 
python 学习记录

#configparse 模块
ConfigParser 模块为常用的操作ini文件的模块，但是存在一些缺陷，无法识别section的大小写，无法读取文件注释，这样修带有注释的配置文件时就会存在问题。

#configobj模块
正常的读配置文件的方法是给ConfigObj一个文件名，然后通过字典来访问成员，子段来获取value值，不会存在注释无法读取的缺陷

	pip install configobj

#mysql 数据库封装
安装 pymysql 库
	
	pip install pymysql

