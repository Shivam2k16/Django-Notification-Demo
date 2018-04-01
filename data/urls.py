from django.conf.urls import include, url
from django.contrib import admin

from data import views

urlpatterns = [

    url(r'^addtruck/$',views.addtruck,name='truck' ),
    url(r'^notification/$',views.notification,name='notification' ),
    url(r'^notification/(?P<pk>[\w-]+)/$',views.notification_mark,name='notification_mark'),
]
