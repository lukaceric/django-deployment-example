from django.conf.urls import url
from basic_app2 import views
from django.urls import path

app_name = 'basic_app2'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]
