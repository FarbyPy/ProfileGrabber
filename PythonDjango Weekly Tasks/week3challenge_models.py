from django.db import models

# Create your models here.
class SavedUser(models.Model):
	source = models.CharField(max_length=16)
	handle = models.CharField(max_length=100, unique=True)
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	influencer = models.CharField(max_length=16)
	followers = models.IntegerField()
	following = models.IntegerField()
	description = models.TextField()
	def __str__(self):
		return self.handle

class Tweets(models.Model):
	user_name = models.ForeignKey(SavedUser)
	tweet_text = models.CharField(max_length=140)
	def __str__(self):
		return self.tweet_text

		
	