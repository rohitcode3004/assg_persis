from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Created a Profile class which is linked to user table of database.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return(self.user.username, "profile")