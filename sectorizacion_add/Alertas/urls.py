
#from django.conf.urls import  url
from django.urls import path
from . import views

urlpatterns = [
    
   # url(r'^luna/$', views.luna),
   path('luna/', views.luna),


]