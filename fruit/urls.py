from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
admin.autodiscover()
urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^shakes/',include('shakes.urls')),
    path('shakes/', include('django.contrib.auth.urls')),
    url(r'^accounts/',include('shakes.urls')),
]
urlpatterns+=staticfiles_urlpatterns()