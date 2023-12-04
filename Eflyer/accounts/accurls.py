from django.urls import path
from . import views



urlpatterns = [
    path("", views.usr_reg, name="register"),
    path("login", views.login_page, name="login"),
    

  

    
    
]