from django.urls import path
from . import views

urlpatterns = [
	path('', views.list, name="list"),
	path('login/', views.user_login, name="login"),
	path('register/', views.user_register, name="register"),
	path('newpass/<str:key>/',views.user_new_pass, name='userNewpass')


]
