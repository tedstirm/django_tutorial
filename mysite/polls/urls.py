from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('', 
		# ex: /polls/
		url(r'^$', views.index, name='index'),
		# ex: polls/5/
		url(r'^(?P<pk>\d+)/$', views.detail, name = 'detail'),
		# ex: /polls/5/results/
    	url(r'^(?P<pk>\d+)/results/$', views.results, name='results'),
    	# ex: /polls/5/vote/
    	url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'),
	)