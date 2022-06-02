from django.db import models

class Contact(models.Model):
	numele = models.CharField(max_length=60, blank=False)
	prenumele = models.CharField(max_length=120, blank=False)
	email = models.EmailField(max_length=60, blank=False)
	mesajul = models.CharField(max_length=300, blank=False)

	def __str__(self):
		return f"{self.numele} {self.prenumele}"