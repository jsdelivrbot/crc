from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'teledm'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='teledm/home.html'), name='home'),
    url(r'^mapViewer/$', views.mapViewer, name='mapViewer'),
    url(r'^mapDist/$', views.mapDist, name='mapDist'),
    url(r'^calval/$', views.calval, name='calval'),
    url(r'^localisation/$', TemplateView.as_view(template_name='teledm/localisation.html'), name='localisation'),
    ###tuto
    url(r'^DB/$', TemplateView.as_view(template_name='teledm/db.html'), name='DB'),
    url(r'^traitementsData/$', TemplateView.as_view(template_name='teledm/traitementsData.html'), name='traitementsData'),
    url(r'^tutoMap/$', TemplateView.as_view(template_name='teledm/tutoMap.html'), name='tutoMap'),
    url(r'^tutoCalVal/$', TemplateView.as_view(template_name='teledm/tutoCalVal.html'), name='tutoCalVal'),
    url(r'^tutoExtraction/$', TemplateView.as_view(template_name='teledm/tutoExtraction.html'), name='tutoExtraction'),
    url(r'^stationsAeronetTeom/$', TemplateView.as_view(template_name='teledm/stations.html'), name='stations'),
]
