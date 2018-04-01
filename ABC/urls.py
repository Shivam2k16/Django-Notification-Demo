from django.conf.urls import include, url
from django.contrib import admin

from ABC import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ABC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^data/',include('data.urls')),
    url(r'^$',views.home,name='home' ),
]
