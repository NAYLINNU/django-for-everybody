from django.urls import path
from cookieapp import views

urlpatterns =[
    path('cookie', views.cookie),
    path('', views.sessfun),
]