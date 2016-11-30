from django.conf.urls import url
from . import views

app_name = 'dev'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^location/(?P<country>[A-Za-z\- ]+)/$', views.location, name = 'location'),
    # url(r'^location/(?P<country>[a-z\- ]+)/$', views.location, name = 'location'),
    url(r'^location/$', views.location, name = 'location'),
    url(r'^pic/(?P<country>[a-z,\- ]+)\+(?P<variable>[A-Z0-9.]+)/$', views.pic, name = 'pic'),
    url(r'^pic/$', views.pic, name = 'pic'),
    # url(r'^indicator/(?P<country>[a-z,\- ]+)\+(?P<variable>[A-Z.]+)/$', views.indicator, name = 'indicator'),
    url(r'^indicator/$', views.indicator, name = 'indicator'),
    url(r'^correlate/$', views.correlate, name = 'compare'),
    url(r'^scatter/(?P<variable>[A-Z0-9.]+)/$', views.scatter, name = 'scatter'),

    url(r'^team', views.team, name = 'team'),
    url(r'^question', views.question, name = 'question'),
    url(r'^datasetsource', views.datasetSource, name = 'datasetSource')
]
