from django.conf.urls import url
from . import views
app_name = 'epinmain'
urlpatterns = [
    url(r'^login/$', views.login,name= 'login'),
]