from django.db import models

# Create your models here.
class App1(models.Model):
	action =		 models.CharField(max_length=200)
	choice = 		 models.ForeignKey('Choice')
	def __unicode__(self):
	    return self.action

class Choice(models.Model):
	choice_text =		 models.CharField(max_length=200)
	

	def __unicode__(self):
	    return self.choice_text