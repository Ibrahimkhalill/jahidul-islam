
from django.db import models
from django.utils import timezone

# Create your models here.


class Image(models.Model):
  image = models.ImageField()
  category = models.CharField(max_length=50,null=True,blank=True)
	

def __str__(self):
		return self.category

@property
def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class Mesaage(models.Model):
	name = models.CharField(max_length=100)
	email = models.TextField()
	subject = models.TextField()
	text = models.TextField()
	date_timefield = models.DateTimeField(default=timezone.now)
  

	def __str__(self):
		return self.email
 