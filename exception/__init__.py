#!usr/bin/env python

if __name__ == '__main__':
	# print('exception 测试');
	try:
		raise Exception('name',1,3,3); #抛出错误
	except Exception as e:
		print(e.args[0:])   #输出错误提示   e.args 元组
	else:
		pass
	finally:
		pass
	
	pass;
else:
	print('正在加载 exception 模块······');
	print('加载 exception 模块完成');