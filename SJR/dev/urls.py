from django.conf.urls import url
from . import views

app_name = 'dev'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^location/(?P<country>[A-Za-z\- ]+)/$', views.location, name = 'location'),
    url(r'^location/(?P<country>[a-z\- ]+)/$', views.location, name = 'location'),
    url(r'^location/$', views.location, name = 'location'),
    url(r'^form/(?P<country>[a-z\- ]+)/$', views.form, name = 'form'),
    url(r'^form/$', views.form, name = 'form'),
    # url(r'^pic/(?P<country>[a-z\- ]+)/$', views.pic, name = 'pic'),
    # url(r'^pic/(?P<country>[A-Za-z\- ]+)/$', views.pic, name = 'pic'),
    url(r'^pic/$', views.pic, name = 'pic'),
    url(r'^indicator/$', views.indicator, name = 'indicator'),
    url(r'^correlate/$', views.correlate, name = 'compare')

]
