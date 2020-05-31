from django.urls import path
from myauth import views

urlpatterns = [
    path('login/', views.auth_login, name='auth_login'),
]

