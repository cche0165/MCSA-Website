#处理url
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^helloworld/', include('helloworld.urls')),
    url(r'^admin/', admin.site.urls),
]