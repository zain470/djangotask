from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('base/',views.base,name='base'),

    path('buy/',views.buyc,name='buy'),

    path('buy/',views.buy,name='buy'),

    
    
]