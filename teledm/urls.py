from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

import views

app_name = 'teledm'
urlpatterns = [
    ###pages
    url(r'^validation$', views.validation, name='validation'),
    #url(r'^emailValidation$', views.emailValidation, name='emailValidation'),
    url(r'^$', TemplateView.as_view(template_name='teledm/home.html'), name='home'),
    url(r'^mapViewer/$', views.mapViewer, name='mapViewer'),
    url(r'^mapDist/$', views.mapDist, name='mapDist'),
    url(r'^calval/$', views.calval, name='calval'),
    url(r'^localisation/$', TemplateView.as_view(template_name='teledm/localisation.html'), name='localisation'),
    ###proxy
    url(r'^proxyajax/(?P<path>.*)$', views.proxyAjax, name='mapViewer'),
    url(r'^minmax/(?P<path>.*)$', views.minmax, name='minmax'),
    url(r'^dates/(?P<path>.*)$', views.dates, name='mapViewer'),
    url(r'^proxywms/(?P<path>.*)$', views.proxyWMS, name='mapViewer'),
    url(r'^proxydownload/(?P<path>.*)$', views.proxyDownload, name='mapViewer'),
    url(r'^colorbar/(?P<path>.*)$', views.colorbar, name='colorbar'),
    url(r'^proxyncss/(?P<path>.*)$', views.proxyNCSS, name='mapViewer'),
    ###script download
    url(r'^nc2txtPy/$', views.nc2txtPy, name='nc2txtPy'),
    url(r'^nc2txtR/$', views.nc2txtR, name='nc2txtR'),
    url(r'^scriptPy/$', views.scriptPy, name='scriptPy'),
    url(r'^scriptR/$', views.scriptR, name='scriptR'),
    ###tuto
    url(r'^charteTeleDM/$', TemplateView.as_view(template_name='teledm/charteTeleDM.html'), name='charteTeleDM'),
    url(r'^DB/$', TemplateView.as_view(template_name='teledm/database.html'), name='DB'),
    url(r'^traitementsData/$', TemplateView.as_view(template_name='teledm/traitementsData.html'), name='traitementsData'),
    url(r'^tutoMap/$', TemplateView.as_view(template_name='teledm/tutoMap.html'), name='tutoMap'),
    url(r'^tutoCalVal/$', TemplateView.as_view(template_name='teledm/tutoCalVal.html'), name='tutoCalVal'),
    url(r'^tutoExtraction/$', TemplateView.as_view(template_name='teledm/tutoExtraction.html'), name='tutoExtraction'),
    url(r'^stationsAeronetTeom/$', TemplateView.as_view(template_name='teledm/stations.html'), name='stations'),
]
