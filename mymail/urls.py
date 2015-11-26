from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', 'mymail.views.home'),
    url(r'^registration/$', 'mymail.views.registered'),
		url(r'^validate/$', 'mymail.views.user_validate'),
		# url(r'^validate/$', 'mymail.views.user_validate'),   
    # url(r'^login', 'mymail.views.login'),
]