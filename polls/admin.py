from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

#1 Basic way of registering model in Admin
#admin.site.register(Choice)

#2 Delicate way of multiplce choice registration, inheriting admin.StackedInline
# class ChoiceInline(admin.StackedInline):
# 	#override model variable to define what model attributes are to be shown. 
# 	model = Choice
# 	#override extrac variable to define the number of regi-forms
# 	extra = 4 

#3 change the display type to TabularInline
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 4 

class QuestionAdmin(admin.ModelAdmin):
	#1 changing order of fields
	#fields = ['pub_date', 'question_text']

	#2 Split form up into fieldsets
	fieldsets = [

		(None,	{'fields':['question_text']}),
		('Date information',{'fields':['pub_date'],'classes':['collapse']}),

	]
	inlines = [ChoiceInline]
	
	#Add list view of change list by overriding
	list_display = ('question_text','pub_date','was_published_recently')
	#Add Filter sidebar of change list by ovveriding
	list_filter = ['pub_date']

	#Add search Capability
	search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)

