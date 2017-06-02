from django.db import models
from django.utils import timezone
import datetime

#django.db.models.Model 

# Create your models here.
class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	#add a few attributes to sort by list_display by this method.
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	#Choice class is related to a single Question
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

	#Activating models based on the class information. 
	#but we need to tell our project that the polls app is installed. 