from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Banner(models.Model):
	banner_image = models.CharField(max_length=50)


class About_us(models.Model):

	name = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	intro = models.TextField()
	image = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	

class Products(models.Model):
	name = models.CharField(max_length=50)
	image = models.CharField(max_length=100,null=True, blank=True)
	def __str__(self):
		return self.name


class ProductDetail(models.Model):


	name = models.CharField(max_length=50)
	image=models.CharField(max_length=100,null=True, blank=True)
	product_number = models.CharField(max_length=50)
	calorie = models.CharField(max_length=50)
	weight = models.CharField(max_length=50)
	information = models.TextField()
	otherimages1 = models.CharField(max_length=100,null=True, blank=True)
	otherimages2 = models.CharField(max_length=100,null=True, blank=True)
	otherimages3 = models.CharField(max_length=100,null=True, blank=True)

	def __str__(self):
		return self.name



class News(models.Model):

	title=models.CharField(max_length=200)
	href=models.TextField(default= '#')
	published_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title



class Contact(models.Model):
	
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	text = models.TextField()

	def __str__(self):
		return self.name


class QA(models.Model):
	
	question = models.TextField()
	answer = models.TextField()

	def __str__(self):
		return self.question



