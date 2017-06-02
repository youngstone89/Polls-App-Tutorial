from django.conf.urls import url 
from . import views


#add app_name to tell Django to diffenciate which app view to create
app_name='polls'

#After app_name specified here, you need to point namespaced view in view page
urlpatterns=[ 
	#exclude /polls/
	url(r'^$',views.IndexView.as_view(), name="index"),

	#exclude /polls/5/
	#Change questions_id to pk in case of using generic view
	#views.{generic view type}.as_view() to use Generic View
	url(r'^detail/(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name="detail"),

	#exclude /polls/5/results
	#Change questions_id to pk in case of using generic view
	#views.{generic view type}.as_view() to use Generic View
	url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(), name="results"),

	#exclude /polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name="vote"),

]