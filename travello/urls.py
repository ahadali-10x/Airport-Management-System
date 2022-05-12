from django.urls import path

from . import views
app_name = "main" 

urlpatterns = [
    path('',views.home,  name = 'home'),
    path('login',views.login_request,  name = 'login'),
    path('register', views.register_request, name="register"),
    path('home',views.home,  name = 'home'),
    path('user',views.user,  name = 'user'),
    #path('admin_new',views.admin_new,  name = 'admin_new')
]