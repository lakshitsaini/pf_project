from django.db import models
class blog(models.Model):
	title=models.CharField(max_length=200)
	#pub_date=models.DateTimeField
	body=models.TextField()
	image=models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]
# Create your models here.
