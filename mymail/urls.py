from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', 'mymail.views.home'),
    url(r'^registration/$', 'mymail.views.registered'),
		url(r'^validate/inbox/$', 'mymail.views.user_validate'),
		url(r'^success/$', 'mymail.views.success_login'),
		url(r'^success/inbox/$', 'mymail.views.inbox_mail'),
		url(r'^success/new_mail/$', 'mymail.views.new_mail'),
		url(r'^success/sentmail/$', 'mymail.views.sent_mail'),
		url(r'^success/trash/$', 'mymail.views.trash_mail'),
		url(r'^validate/(inbox)/sent_success/$', 'mymail.views.sending'),
		url(r'^success/(inbox|sentmail|trash|)/sent_success/$', 'mymail.views.sending'),
		url(r'^validate/inbox/(?P<mail_id>\d+)/$', 'mymail.views.displaying'),
		url(r'^success/(sentmail|inbox|trash)/(?P<mail_id>\d+)/$', 'mymail.views.displaying'),
		url(r'^validate/inbox/del/(?P<mail_id>\d+)/$', 'mymail.views.displaying'),
		url(r'^success/(sentmail|inbox)/del/(?P<mail_id>\d+)/$', 'mymail.views.trashing'),
]