
class A:
	
	def play(ad,b = ''):
		print(dir(ad))
		ad.name()
		print(b)


	def name(self):
		print('本身');

	def age():
		print('18')

a = A();
a.play('adasd');
# a.age();