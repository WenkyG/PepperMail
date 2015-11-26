from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^create_account', 'mymail.views.registration'),
    # url(r'^login', 'mymail.views.login'),
]