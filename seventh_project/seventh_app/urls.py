from django.urls import path
from seventh_app import views

app_name = 'seventh_app'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('user_login/', views.user_login, name = 'user_login')
]
