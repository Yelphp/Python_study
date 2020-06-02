from django.db import models

# Create your models here.

# 用户表
class User(models.Model):
	sort = models.IntegerField()
	name = models.CharField(max_length=30)
	age = models.IntegerField(default=0)

	def __str__(self):
		return self.name
