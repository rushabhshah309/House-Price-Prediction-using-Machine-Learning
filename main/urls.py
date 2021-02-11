from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('about/', views.about, name='about'),
    path('predict1/', views.predict1, name='predict1'),
    path('data/', views.data, name='data'),
]
