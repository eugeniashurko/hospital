from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hospital.views.index', name='index'),
    url(r'^login/', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout/', 'django.contrib.auth.views.logout'),
    url(r'^history/', include('histories.urls')),
    url(r'^calendar/', 'hospital.views.calendar', name="calendar"),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^admin/', include(admin.site.urls))
)

