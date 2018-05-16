from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.enhance_home, name='enhance')
] 