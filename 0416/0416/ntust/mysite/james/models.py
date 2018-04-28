from django.db import models

# Create your models here.

class Name(models.Model):

	person			= models.CharField(max_length = 30)

	def __str__(self):
		return self.person

class Birthday(models.Model):

	year 			= models.CharField(max_length = 5)
	month			= models.CharField(max_length = 3)
	day				= models.CharField(max_length = 3)
	name 			= models.ForeignKey(Name)

	def __str__(self):
		return self.year

class Gender(models.Model):

	Female_Male  	= models.CharField(max_length = 7) 
	name			= models.ForeignKey(Name)

	def __str__(self):
		return self.Female_Male
	#python manage.py makemigrations james
	#python manage.py sqlmigrate james 0001
	#python manage.py migrate