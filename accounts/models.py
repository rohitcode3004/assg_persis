from django.db import models


class Router(models.Model):
	sapid = models.CharField(max_length = 100, null =True, blank=True)
	hostname = models.CharField(max_length = 100, null =True, blank=True)
	loopback = models.CharField(max_length = 100, null =True, blank=True)
	mac_address = models.CharField(max_length = 100, null =True, blank=True)

	def __str__(self):
		return(self.hostname)