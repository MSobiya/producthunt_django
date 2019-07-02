from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	title = models.CharField(max_length = 100)
	url = models.TextField()
	publish_date = models.DateTimeField()
	image = models.ImageField(upload_to = 'images/')
	icon = models.ImageField(upload_to = 'images/')
	body = models.TextField()
	votes = models.IntegerField(default=0)
	#hunter is a user who upload the product.
	#hunter is a foreign key here because user is already registered in User database.
	#Main aim to use it as foreign key is to ensure tha only registered user can post the Product.
	hunter = models.ForeignKey(User, on_delete = models.CASCADE)
	#on_delete = models.CASCADE indicates product will be delete if user of product delete from User table.
	 



	def summary(self):
		return self.body[:50]

	def pretty_date(self):
		return self.publish_date.strftime('%b %e, %Y')


	def __str__(self):
		return self.title